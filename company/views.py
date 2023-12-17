from django.shortcuts import render,redirect
from .forms import ClientForm,InternForm,ExpenseForm,CustomerInvoice
from .models import Customer,Expense,Invoice
from django.core.paginator import Paginator
from datetime import date
from datetime import datetime
from django.db.models import Sum

# Create your views here.
def dashboard(request):

    client_total=Customer.objects.filter(customer_type='client').count()
    intern_total=Customer.objects.filter(customer_type='intern').count()

    context={'client_total':client_total,'intern_total':intern_total}
    return render(request,'company/dashboard.html',context)



def client_list(request):

    search=request.GET.get('search')
    if search:
        client_list=Customer.objects.filter(customer_type='client',name__icontains=search)

    else:
        client_list=Customer.objects.filter(customer_type='client')
    context={'client_list':client_list}
    return render(request,'company/client_list.html',context)



def client_form(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company:client-list')
    context={'form':form,'client':'client'}
    return render(request,'company/customer_form.html',context)

def client_update(request,id):
    client=Customer.objects.filter(customer_type='client').get(id=id)
   
    invoice_list=Invoice.objects.filter(customer=client)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('company:client-list')
    context={'form':form,'client_update':'client_update','client':client,'invoice_list':invoice_list}
    return render(request,'company/customer_detail_update.html',context)

def client_delete(request,id):

    client=Customer.objects.filter(customer_type='client').get(id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('comapny:client-list')
    context={'client_delete':'client_delete','client':client}
    return render(request,'company/customer_delete.html',context)

def client_invoice(request,id):

    client=Customer.objects.filter(id=id).first()
    print(type(client.id))
    form=CustomerInvoice(instance=client,initial={'customer':client})

    if request.method=='POST':
        form=CustomerInvoice(request.POST)
        if form.is_valid():
            myform=form.save()
            print()     
            return redirect('company:client-update',client.id)

    context={'form':form,client:client,'client_invoice':'client_invoice','client':client}
    return render(request,'company/customer_invoice.html',context)


def client_invoice_delete(request,client_id,invoice_id):
      client=Customer.objects.get(id=client_id)
      invoice=Invoice.objects.filter(id=invoice_id)
      invoice.delete()
      return redirect('company:client-update',client.id)

def intern_invoice(request,id):
    intern=Customer.objects.filter(id=id).first()
    form=CustomerInvoice(instance=intern,initial={'customer':intern})

    if request.method=='POST':
        form=CustomerInvoice(request.POST)
        
        if form.is_valid():
            form.save()
            # customer_invoice.customer=client
            return redirect('company:intern-update',intern.id)

    context={'form':form,'intern':intern}
    return render(request,'company/customer_invoice.html',context)


def intern_invoice_delete(request,intern_id,invoice_id):
      intern=Customer.objects.get(id=intern_id)
      invoice=Invoice.objects.filter(id=invoice_id)
      invoice.delete()
      return redirect('company:intern-update',intern.id)

def intern_list(request):

    search=request.GET.get('search')
    if search:
        intern_list=Customer.objects.filter(customer_type='intern',name__icontains=search)
    else:
        intern_list=Customer.objects.filter(customer_type='intern')

    context={'intern_list':intern_list}
    return render(request,'company/intern_list.html',context)

def intern_form(request):
    form=InternForm()
    if request.method=='POST':
        form=InternForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company:intern-list')
    context={'form':form}
    return render(request,'company/customer_form.html',context)

def intern_update(request,id):
    intern=Customer.objects.filter(customer_type='intern').get(id=id)
    
    invoice_list=Invoice.objects.filter(customer=intern)

    form=InternForm(instance=intern)
    if request.method=='POST':
        form=InternForm(request.POST,instance=intern)
        if form.is_valid():
            form.save()
            return redirect('company:intern-list')
    context={'form':form,'intern':intern,'invoice_list':invoice_list}
    return render(request,'company/customer_detail_update.html',context)



def intern_delete(request,id):
    intern=Customer.objects.filter(customer_type='intern').get(id=id)
    if request.method=="POST":
        intern.delete()
        return redirect('company:intern-list')
    context={'intern':intern}
    return render(request,'company/customer_delete.html',context)

def expense_list(request):
    expense_list=Expense.objects.all()

    context={'expense_list':expense_list}
    return render(request,'company/expenses_list.html',context)

def expense_form(request):
    form=ExpenseForm()
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company:expense-list')
    context={'form':form}
    return render(request,'company/expenses_form.html',context)
    
def invoice_list(request):

    search=request.GET.get('search')
    if search:
       invoice_list=Invoice.objects.filter(customer__name__icontains = search)
    else:
        invoice_list=Invoice.objects.all()

    context={'invoice_list':invoice_list}
    return render(request,'company/invoice_list.html',context)


def report_income_expenses(request):

    total_income=Invoice.objects.aggregate(Sum('amount'))
    total_expenses=Expense.objects.aggregate(Sum('amount'))
    invoice=Invoice.objects.all()
    expense=Expense.objects.all()

    if request.method=='POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if  end_date is '' :
             end_date=date.today()
        # print(start_date_str,end_date_str)
        # start_date = datetime.strptime(str(start_date_str), '%Y-%m-%d').date()
        # end_date = datetime.strptime(str(end_date_str), '%Y-%m-%d').date()
        
        invoices=Invoice.objects.filter(invoice_date__range=(start_date, end_date))
        expenses = Expense.objects.filter(date__range=(start_date, end_date))

        total_income=Invoice.objects.filter(invoice_date__range=(start_date, end_date)).aggregate(Sum('amount'))



        context={'total_income':int(total_income['amount__sum']),'total_expenses':int(total_expenses['amount__sum']),
             'invoices':invoices,'expenses':expenses}
        
        return render(request,'company/report_list.html',context)

  
    context={'total_expenses':int(total_expenses['amount__sum']),
            }
    return render(request,'company/report_list.html',context)

