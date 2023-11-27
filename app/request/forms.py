from django import forms

from .models import Requete

class RequeteForm(forms.ModelForm):
    staff_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    choix_d = [("rh", "HR"), ("technique", "Network"), ("sales", "Commercial & Marketing"), ("finance", "Finance")]
    department = forms.ChoiceField(choices = choix_d)
    
    project_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    choix_t = [("installation", "Installation"), ("service_repair", "Service/Repair"), ("transfer", "Transfer"), ("sale", "Sale")]
    type_service = forms.ChoiceField(choices = choix_t, widget = forms.RadioSelect)
    
    customer = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    choix_m = [("test", "Test")]
    manager_signature = forms.ChoiceField(choices = choix_m)
    
    choix_l = [("test", "Test")]
    line_manager_name = forms.ChoiceField(choices = choix_l)
    
    items_recieved_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    items_recieved_signature = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    choix_i = [("test", "Test")]
    issued_name = forms.ChoiceField(choices = choix_i)
    
    class Meta:
        model = Requete
        fields = ('staff_name', 'department', 'project_code', 'type_service', 'customer', 'location', 
                  'manager_signature', 'line_manager_name', 'items_recieved_name', 'items_recieved_signature', 'issued_name')           