from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.IntegerField()
    department = models.CharField (max_length=255, choices=[
        ("rh", "HR"),
        ("technique", "Network"),
        ("sales", "Commercial & Marketing"),
        ("finance", "Finance"),
    ], default='sales')
    
    def __str__(self):
        return self.user.username
