from django.shortcuts import render,redirect
from .forms import LoginForm,CompanyRegisterForm
from django.contrib.auth import login,authenticate,logout
from .models import Company
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('company:dashboard')
    else:
        form=LoginForm()
        if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('company:dashboard')
    context={'form':form}
    return render(request,'myadmin/login_form.html',context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def company_register(request):
    
    form=CompanyRegisterForm()
    if request.method=='POST':
        form=CompanyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'myadmin/login_form.html',context)

@login_required
def company_list(request):

    search=request.GET.get('search')

    if search:
        companylist=Company.objects.filter(name__icontains=search)
    else:
        companylist=Company.objects.all()

    context={'company_list':companylist}
    return render(request,'myadmin/company_list.html',context)

@login_required
def company_profile(request):
    return render(request,'myadmin/register_form.html')