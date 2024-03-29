from django.shortcuts import render,redirect
from .forms import ClientForm,InternForm,ExpenseForm,CustomerInvoice
from .models import Customer,Expense,Invoice
from django.core.paginator import Paginator
from datetime import date

from django.db.models import Sum
from myadmin.models import Company
from django.contrib.auth.decorators import login_required


from django.http import FileResponse,HttpResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.
def render_to_pdf(invoice):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="invoice_{invoice.invoice_no}.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response, pagesize=letter)

    # Add content to the PDF
    p.drawString(100, 800, f"Invoice {invoice.invoice_no}")
    p.drawString(100, 780, f"Customer Name: {invoice.customer}")
    p.drawString(100, 760, f"Date: {invoice.invoice_date}")
    p.drawString(100, 740, f"Amount: {invoice.amount}")
    # Add other invoice details as needed

    # Close the PDF object cleanly, and return the response.
    p.showPage()
    p.save()
    return response

def invoice_pdf(request,invoice_id):
    invoice=Invoice.objects.get(id=invoice_id)
    return render_to_pdf(invoice)




@login_required
def dashboard(request):

    client_total=Customer.objects.filter(user=request.user,customer_type='client').count()
    intern_total=Customer.objects.filter(user=request.user,customer_type='intern').count()
    total_company=Company.objects.all().count()

    context={'client_total':client_total,'intern_total':intern_total,'total_company':total_company}
    return render(request,'dashboard.html',context)


@login_required
def client_list(request):

    search=request.GET.get('search')
    sort_order=request.GET.get('sort_order')
    

    if search:
        client_list=Customer.objects.filter(user=request.user,customer_type='client',name__icontains=search).order_by('registered_date')

    else:
        if sort_order == 'ascending':
            client_list=Customer.objects.filter(user=request.user,customer_type='client').order_by('-registered_date')
        else:
            client_list=Customer.objects.filter(user=request.user,customer_type='client').order_by('registered_date')
    context={'client_list':client_list}
    return render(request,'company/client_list.html',context)




@login_required
def client_form(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.user=request.user
            customer.save()
            return redirect('company:client-list')
    context={'form':form,'client':'client','client_form':'client_form'}
    return render(request,'company/customer_form.html',context)

@login_required
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

@login_required
def client_delete(request,id):

    client=Customer.objects.filter(customer_type='client').get(id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('company:client-list')
    context={'client_delete':'client_delete','client':client}
    return render(request,'company/customer_delete.html',context)



@login_required
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

@login_required
def client_invoice_delete(request,client_id,invoice_id):
      
      client=Customer.objects.get(id=client_id)
      invoice=Invoice.objects.filter(id=invoice_id)
      invoice.delete()
      return redirect('company:client-update',client.id)

@login_required
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

@login_required
def intern_invoice_delete(request,intern_id,invoice_id):
      
      intern=Customer.objects.get(id=intern_id)
      invoice=Invoice.objects.filter(id=invoice_id)
      invoice.delete()
      return redirect('company:intern-update',intern.id)

@login_required
def intern_list(request):

    search=request.GET.get('search')
    if search:
        intern_list=Customer.objects.filter(user=request.user,customer_type='intern',name__icontains=search)
    else:
        intern_list=Customer.objects.filter(user=request.user,customer_type='intern')

    context={'intern_list':intern_list}
    return render(request,'company/intern_list.html',context)

@login_required
def intern_form(request):
    form=InternForm()
    if request.method=='POST':
        form=InternForm(request.POST)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.user=request.user
            customer.save()
            return redirect('company:intern-list')
    context={'form':form}
    return render(request,'company/customer_form.html',context)

@login_required
def intern_update(request,id):

    intern=Customer.objects.filter(user=request.user,customer_type='intern').get(id=id)
    
    invoice_list=Invoice.objects.filter(customer__user=request.user,customer=intern)

    form=InternForm(instance=intern)
    if request.method=='POST':
        form=InternForm(request.POST,instance=intern)
        if form.is_valid():
            form.save()
            return redirect('company:intern-list')
    context={'form':form,'intern':intern,'invoice_list':invoice_list}
    return render(request,'company/customer_detail_update.html',context)


@login_required
def intern_delete(request,id):

    intern=Customer.objects.filter(customer_type='intern').get(id=id)
    if request.method=="POST":
        intern.delete()
        return redirect('company:intern-list')
    context={'intern':intern}
    return render(request,'company/customer_delete.html',context)

@login_required
def expense_list(request):

    expense_list=Expense.objects.filter(user=request.user)

    context={'expense_list':expense_list}
    return render(request,'company/expenses_list.html',context)

@login_required
def expense_form(request):
    form=ExpenseForm()
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            expense=form.save(commit=False)
            expense.user=request.user
            expense.save()
            return redirect('company:expense-list')
    context={'form':form,'add_expense':'add_expense'}
    return render(request,'company/expenses_form.html',context)

@login_required
def expense_update(request,id):
    expense=Expense.objects.get(id=id)
    form=ExpenseForm(instance=expense)
    if request.method=='POST':
        form=ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('company:expense-list')
    context={'form':form}
    return render(request,'company/expenses_form.html',context)

@login_required
def expense_delete(request,id):
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('company:expense-list')



@login_required 
def invoice_list(request):

    search=request.GET.get('search')
    if search:
       invoice_list=Invoice.objects.filter(customer__user=request.user,customer__name__icontains = search)
    else:
        invoice_list=Invoice.objects.filter(customer__user=request.user)

    context={'invoice_list':invoice_list}
    return render(request,'company/invoice_list.html',context)

@login_required
def report_income_expenses(request):

    total_income=Invoice.objects.aggregate(Sum('amount'))
    total_expenses=Expense.objects.aggregate(Sum('amount'))
    invoice=Invoice.objects.filter(customer__user=request.user)
    expense=Expense.objects.filter(user=request.user)

    if request.method=='POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if  not end_date:
             end_date=date.today()
        # print(start_date_str,end_date_str)
        # start_date = datetime.strptime(str(start_date_str), '%Y-%m-%d').date()
        # end_date = datetime.strptime(str(end_date_str), '%Y-%m-%d').date()
        
        invoices=Invoice.objects.filter(customer__user=request.user,invoice_date__range=(start_date, str(end_date)))
        expenses = Expense.objects.filter(date__range=(start_date, end_date))

        total_income_sum=Invoice.objects.filter(customer__user=request.user,invoice_date__range=(start_date, end_date)).aggregate(Sum('amount'))
        # total_income=total_income_sum.get('amount__sum',0)
            
        total_income = total_income_sum.get('amount__sum', 0)
        if total_income is not None:
            balance= total_income -  total_expenses['amount__sum']
        else:
            balance=0

        context={'total_income':total_income,'total_expenses':str(total_expenses['amount__sum']),
             'invoices':invoices,'expenses':expenses,'balance':balance}
        
        return render(request,'company/report_list.html',context)

  
    context={'total_expenses':str(total_expenses['amount__sum']),
            }
    return render(request,'company/report_list.html',context)

def client_report(request):

    if request.method=='POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if  not end_date:
            end_date=date.today()

        client_list=Customer.objects.filter(customer_type='client',joining_date__range=(start_date, str(end_date)))
        total_client=client_list.count()
        context={'client_list':client_list,'total_client':total_client}
        return render(request,'company/client_report.html',context)

    return render(request,'company/client_report.html')

def intern_report(request):

    if request.method=='POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not end_date:
            end_date=date.today()

        intern_list=Customer.objects.filter(customer_type='intern',joining_date__range=(start_date, str(end_date)))
       
        total_intern=intern_list.count()
        context={'intern_list':intern_list,'total_intern':total_intern}
        return render(request,'company/intern_report.html',context)
    
    return render(request,'company/intern_report.html')

def expense_report(request):
    if request.method=='POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
 
        if not end_date:
            end_date=date.today()
        expense_list=Expense.objects.filter(user=request.user,date__range=(start_date,str(end_date)))
        total_expenses=Expense.objects.filter(user=request.user,date__range=(start_date,str(end_date))).aggregate(Sum('amount'))
        context={'expense_list':expense_list,'total_expenses':total_expenses['amount__sum']}
        return render(request,'company/expense_report.html',context)
    return render(request,'company/expense_report.html')