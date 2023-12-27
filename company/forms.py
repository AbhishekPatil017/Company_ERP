from django import forms

from .models import Customer,Expense,Invoice


class DateInput(forms.DateInput):
    input_type='date'

class CustomerInvoice(forms.ModelForm):
    
    customer=forms.Select(attrs={'disabled': 'disabled',})
    invoice_date=forms.DateField(widget=DateInput)

    class Meta:
        model=Invoice
        fields='__all__'

    # def __init__(self,customer,*args,**kwargs):
    #     super(CustomerInvoice,self).__init__(*args,**kwargs)
    #     customer = Customer.objects.filter(id=customer).first()
    #     self.fields['customer'].initial = customer
        


class InternForm(forms.ModelForm):

    customer_type=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    joining_date=forms.DateField(widget=DateInput)
    
    class Meta:
        model=Customer
        fields='__all__'
        
    def __init__(self, *args, **kwargs):
        super(InternForm, self).__init__(*args, **kwargs)
        self.fields['customer_type'].initial = 'intern' 

class ClientForm(forms.ModelForm):
    
    customer_type=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    joining_date=forms.DateField(widget=DateInput)

    class Meta:
        model=Customer
        exclude = ["user"]
        
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['customer_type'].initial = 'client' 

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model=Expense
        fields='__all__'