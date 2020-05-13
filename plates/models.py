from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Plate(models.Model):
    plate_number    = models.CharField(
                            max_length=6, 
                            blank=False, 
                            null=False, 
                            unique=True,
                            validators=[
                                    RegexValidator(
                                                regex='^\\w{6}$', 
                                                message='Length has to be 6', 
                                                code='nomatch'
                                                )
                                    ]
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

class PlateSearch(models.Model):
    search_value = models.CharField(blank=False, null=False, max_length=50)