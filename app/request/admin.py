from django.contrib import admin

from .models import Requete

# Register your models here.

admin.site.register(Requete)

admin.site.site_header = 'Administration'

admin.site.site_title = 'Request'
