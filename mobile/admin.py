from django.contrib import admin

# Register your models here.
from mobile.models import Name

class Nameadmin(admin.ModelAdmin):
    list_display = ['company']

admin.site.register(Name, Nameadmin)