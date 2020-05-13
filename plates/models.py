from django.core.validators import RegexValidator
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('plates:plates-detail', kwargs={"id": self.pk})

    def get_update_url(self):
        return reverse('plates:plates-update', kwargs={"id": self.pk})

    def get_delete_url(self):
        return reverse('plates:plates-delete', kwargs={"id": self.pk})

class PlateSearch(models.Model):
    search_value = models.CharField(blank=False, null=False, max_length=50)