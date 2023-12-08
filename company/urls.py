from django.urls import path
from .views import ( dashboard,
                     client_form,client_list,client_delete,client_update,client_invoice,
                     intern_form,intern_list,intern_update,intern_delete,
                     expense_form,expense_list,
                    invoice_list,)

app_name='company'

urlpatterns = [

    path('',dashboard,name='dashboard'),

    path('clients/',client_list,name='client-list'),
    path('add-client/',client_form,name='add-client'),
    path('update-client/<str:id>/',client_update,name='client-update'),
    path('delete-client/<str:id>/',client_delete,name='client-delete'),
    path('invoice-client/<str:id>/',client_invoice,name='client-invoice'),
    
    path('invoice/',invoice_list,name='invoice-list'),
    
    path('add-intern/',intern_form,name='add-intern'),
    path('interns/',intern_list,name='intern-list'),
    path('intern-update/<str:id>/',intern_update,name='intern-update'),
    path('intern-delete/<str:id>/',intern_delete,name='intern-delete'),

    path('add-expense/',expense_form,name='add-expense'),
    path('expenses/',expense_list,name='expense-list'),

]
