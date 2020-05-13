from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from .forms import PlateSearchForm
from .models import Plate

class PlatesHomeView(View):
	form_class = PlateSearchForm
	#success_url = '.'

	def get(self, request, *args, **kwargs):
		return render(request, 'plates/plates_main.html', {})

	def post(self, request, *args, **kwargs):
		form = PlateSearchForm(request.POST)
		context = {'form': form}
		if form.is_valid():
			return PlatesRawListView().get(request=request, search_value=form.cleaned_data['search_value'])

		return HttpResponseRedirect('list/')

class PlatesRawListView(View):
	template_name = 'plates/plates_list.html'

	def get(self, request, search_value=None, *args, **kwargs):
		
		if search_value is None:
			queryset = Plate.objects.all()
		else:
			queryset_plates = Plate.objects.filter(plate_number__icontains=search_value)
			queryset_first_names = Plate.objects.filter(first_name__icontains=search_value)
			queryset_last_names = Plate.objects.filter(last_name__icontains=search_value)

			queryset = queryset_plates | queryset_first_names | queryset_last_names

		return render(request, self.template_name, {'object_list': queryset})