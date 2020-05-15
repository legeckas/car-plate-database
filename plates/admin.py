from django.contrib import admin

# Register your models here.

from .models import Plate



@admin.register(Plate)

class PlateAdmin(admin.ModelAdmin):
	list_display = ("plate_number", "first_name", "last_name")