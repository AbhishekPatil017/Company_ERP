from django.shortcuts import render,redirect
from .forms import ClientForm,InternForm,ExpenseForm
from .models import Customer,Expense

# Create your views here.
def dashboard(request):
    return render(request,'company/dashboard.html')



def client_list(request):
    client_list=Customer.objects.filter(customer_type='client')
    context={'client_list':client_list}
    return render(request,'company/client_list.html',context)

def client_detail_update(request,id):
    client=Customer.objects.filter(customer_type='client').get(id=id)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('company:client-list')
    context={'client_update':client_update}
    return render(request,'company/customer_detail_update.html',context)

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
    print(client)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('company:client-list')
    context={'form':form,'client_update':'client_update','client':client}
    return render(request,'company/customer_update.html',context)

def client_delete(request,id):
    client=Customer.objects.filter(customer_type='client').get(id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('comapny:client-list')
    context={'client_delete':'client_delete','client':client}
    return render(request,'company/customer_delete.html',context)


def intern_list(request):
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
    form=InternForm(instance=intern)
    if request.method=='POST':
        form=InternForm(request.POST,instance=intern)
        if form.is_valid():
            form.save()
            return redirect('company:intern-list')
    context={'form':form,'intern':intern}
    return render(request,'company/customer_update.html',context)



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
    