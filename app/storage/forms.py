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
        fields = ('show', 'serie', 'description_equipment', 'projet', 'nom_du_fournisseur', 'cout')
        
    show = forms.ModelChoiceField(queryset = Equipment.objects.all(), label ="Description", widget=forms.Select(attrs={
        'class': 'form-control',
    })) 
    serie = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    description_equipment = forms.CharField(widget=forms.TextInput(attrs={
       'class': 'form-control',
    }))    
    projet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    nom_du_fournisseur = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    cout = forms.IntegerField(widget=forms.TextInput(attrs={
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
        fields = ('show', 'quantite',)
        
    show = forms.ModelChoiceField(queryset = Equipment.objects.all(), label ="Description", widget=forms.Select(attrs={
        "hx-get": "load serie/", "hx-target": "#id_serie",
        'class': 'form-control',
    }))    
    quantite = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
"""
class SerieStorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('serie',)
        
    serie = forms.ModelChoiceField(queryset = Storage.objects.none(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
"""
    