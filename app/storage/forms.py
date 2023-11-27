from django import forms

from .models import Storage, Routeur, Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('description',)
    
    choix_d = [("routeur", "routeur"), ("cable", "cable"), ("pc", "pc"), ("switch", "switch")]
    description = forms.ChoiceField(choices = choix_d, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
                                

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('show', 'serie', 'description_equipment', 'code_projet', 'nom_projet', 'client_name', 'site_location', 'nom_du_fournisseur', 'cout')
        
    show = forms.ModelChoiceField(queryset = Equipment.objects.all(), label ="Type", widget=forms.Select(attrs={
        'class': 'form-control',
    })) 
    serie = forms.CharField(label ="Serial number", widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    description_equipment = forms.CharField(widget=forms.TextInput(attrs={
       'class': 'form-control',
    }))    
    code_projet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    nom_projet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    client_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    site_location = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    choix = [("s_1", "supplier 1"), ("s_2", "supplier 2"), ("s_3", "supplier 3"), ("s_4", "supplier 4")]
    nom_du_fournisseur = forms.ChoiceField(choices = choix, label ="Supplier", widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    cout = forms.IntegerField(label ="Cost", widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    

class RouteurForm(forms.ModelForm):
    class Meta:
        model = Routeur
        fields = ('category' ,'quantite_in', 'quantite_out')
        
    quantite_in = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))    
    quantite_out = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))


class DeleteStorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('show', 'quantite')
        
    show = forms.ModelChoiceField(queryset = Equipment.objects.all(), label ="Type", widget=forms.Select(attrs={
        "hx-get": "load serie/", "hx-target": "#id_serie",
        'class': 'form-control',
    }))    
    quantite = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    """serie = forms.CharField(label ="Serial number", widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))"""
    """client_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    site_location = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))"""    
    