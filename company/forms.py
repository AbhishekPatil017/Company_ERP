from django import forms
from .models import Customer,Expense,Invoice


class DateInput(forms.DateInput):
    input_type='date'

class ClientInvoice(forms.ModelForm):
    
    # customer=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    invoice_date=forms.DateField(widget=DateInput)
    class Meta:
        model=Invoice
        fields='__all__'

    # def __init__(self,client,client_id, *args, **kwargs):
    #     super(ClientInvoice, self).__init__(*args, **kwargs)
    #     self.fields['customer']=forms.ModelChoiceField(initial=client_id,queryset=Customer.objects.get(id=client_id))

    def __init__(self,id,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(customer_type='client',id=id)
        


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
        fields='__all__'
        
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['customer_type'].initial = 'client' 

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model=Expense
        fields='__all__'