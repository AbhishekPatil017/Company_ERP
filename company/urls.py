from django.urls import path
from .views import ( dashboard,
                     client_form,client_list,client_delete,client_update,client_invoice,client_invoice_delete,client_report,
                     intern_form,intern_list,intern_update,intern_delete,intern_report,
                     expense_form,expense_list,report_income_expenses,expense_update,expense_delete,
                     invoice_list,intern_invoice,intern_invoice_delete, invoice_pdf)

app_name='company'

urlpatterns = [

    path('',dashboard,name='dashboard'),

    path('clients/',client_list,name='client-list'),
    path('clients-report/',client_report,name='client-report'),
    path('add-client/',client_form,name='add-client'),
    path('update-client/<str:id>/',client_update,name='client-update'),
    path('delete-client/<str:id>/',client_delete,name='client-delete'),
    path('invoice-client/<str:id>/',client_invoice,name='client-invoice'),
    path('client-invoice-delete/<str:client_id>/<str:invoice_id>/',client_invoice_delete,name='client-invoice-delete'),
    
    path('invoice/',invoice_list,name='invoice-list'),
    path('invoice/<str:invoice_id>/pdf/',invoice_pdf,name='invoice-pdf'),
    
    path('add-intern/',intern_form,name='add-intern'),
    path('interns/',intern_list,name='intern-list'),
    path('intern-report/',intern_report,name='intern-report'),
    path('intern-update/<str:id>/',intern_update,name='intern-update'),
    path('intern-delete/<str:id>/',intern_delete,name='intern-delete'),
    path('invoice-intern/<str:id>/',intern_invoice,name='intern-invoice'),
    path('intern-invoice-delete/<str:intern_id>/<str:invoice_id>/',intern_invoice_delete,name='intern-invoice-delete'),
    
    path('add-expense/',expense_form,name='add-expense'),
    path('update-expense/<str:id>/',expense_update,name='update-expense'),
    path('delete-expense/<str:id>/',expense_delete,name='delete-expense'),
    path('expenses/',expense_list,name='expense-list'),

    path('report/',report_income_expenses,name='report')

]
