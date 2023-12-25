from django.shortcuts import render,redirect
from .forms import LoginForm,CompanyRegisterForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('company:dashboard')
    else:
        form=LoginForm()
        if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None and user.is_admin:
                    return redirect('company:dashboard')
                elif user is not None and user.is_company:
                    return redirect('company:dashboard')
    
    context={'form':form}
    return render(request,'myadmin/login_form.html',context)


def logout_user(request):
    pass

def register_user(request):
    form=CompanyRegisterForm()
    
    if request.method=='POST':
        form=CompanyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context={'form':form}
    return render(request,'myadmin/register_form.html',context)