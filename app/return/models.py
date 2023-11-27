from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Return(models.Model):
    staff_name = models.CharField(max_length=100)
    department = models.CharField(max_length=30, choices=[
        ("rh", "HR"),
        ("technique", "Network"),
        ("sales", "Commercial & Marketing"),
        ("finance", "Finance"),
    ], default='sales')
    project_code = models.CharField()
    type_service = models.CharField(max_length=20, choices=[
        ("installation", "Installation"),
        ("service_repair", "Service/Repair"),
        ("transfer", "Transfer"),
        ("sale", "Sale"),
    ], default='installation')
    customer = models.CharField()
    location = models.CharField()
    date_de_creation = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager_signature = models.CharField (max_length=50, choices=[
        ("test", "Test"),
        ], default='test')
    line_manager_name = models.CharField (max_length=50, choices=[
        ("test", "Test"),
        ], default='test')
    items_recieved_name = models.CharField (max_length=50)
    items_recieved_signature = models.CharField (max_length=50)
    issued_name = models.CharField (max_length=50, choices=[
        ("test", "Test"),
        ], default='test')
    issued_signature = models.DateTimeField(auto_now_add=True)
   # supplier = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=[
        ("v", "valide"),
        ("n", "non valide"),
    ], default='n')
    delivery = models.CharField(max_length=30, choices=[
        ("y", "yes"),
        ("n", "no"),
    ], default='n')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=True)
    
    def __str__(self):
        return self.project_code
