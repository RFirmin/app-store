from django.db import models

# Create your models here.

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField()
#    image = models.ImageField(upload_to='storage_image/', null=True, blank=True)

    def __str__(self):
        return self.description
    
    
class Storage(models.Model):
    number = models.AutoField(primary_key=True)
    serie = models.CharField(unique=True)
    description_equipment = models.CharField()
    quantite = models.IntegerField(default=1)
    date_de_livraison = models.DateTimeField(auto_now_add=True)
    projet = models.CharField()
    nom_du_fournisseur = models.CharField()
    cout = models.IntegerField()
#    image = models.ImageField(upload_to='storage_image/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    show =  models.ForeignKey(Equipment, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.serie
    
    
class Routeur(models.Model):
    category = models.CharField(max_length=50)
    quantite_in = models.IntegerField(null=True)
    quantite_out = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category