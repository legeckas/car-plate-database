from django.db import models

# Create your models here.

class Plate(models.Model):
    plate_number    = models.CharField(
                            max_length=6, 
                            blank=False, 
                            null=False, 
                            unique=True
                            )
    first_name      = models.CharField(
                            max_length=50, 
                            blank=False, 
                            null=False
                            )
    last_name       = models.CharField(
                            max_length=50, 
                            blank=False, 
                            null=False
                            )