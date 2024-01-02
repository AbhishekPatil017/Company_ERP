"""
URL configuration for company_erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myadmin.views import login_user,logout_user,company_register,company_list,company_profile,company_password_change

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('company/',include('company.urls')),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('add-company/',company_register,name='add-company'),

    path('company_list/',company_list,name='company-list'),
    path('company_profile/',company_profile,name='company-profile'),
    path('change_password/',company_password_change,name='company-passwordchange')
  
]
