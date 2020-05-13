from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Plate

class PlateListView(ListView):
	template_name = 'plates/plates_list.html'
	queryset = Plate.objects.all()