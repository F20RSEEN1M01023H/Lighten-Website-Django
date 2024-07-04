from django.db import models

# Create your models here.

class Name(models.Model):
    company = models.CharField(max_length=50)
