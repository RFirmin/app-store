from django import forms

from .models import Return

class ReturnForm(forms.ModelForm):
    staff_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    choix = [("rh", "HR"), ("technique", "Network"), ("sales", "Commercial & Marketing"), ("finance", "Finance")]
    department = forms.ChoiceField(choices = choix)
    
    project_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    chois = [("installation", "Installation"), ("service_repair", "Service/Repair"), ("transfer", "Transfer"), ("sale", "Sale")]
    type_service = forms.ChoiceField(choices = chois, widget = forms.RadioSelect)
    
    customer = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    manager_signature = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    line_manager_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    items_recieved_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    items_recieved_signature = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    issued_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = Return
        fields = ('staff_name', 'department', 'project_code', 'type_service', 'customer', 'location', 
                  'manager_signature', 'line_manager_name', 'items_recieved_name', 'items_recieved_signature', 'issued_name')           