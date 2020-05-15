from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

from django.views.generic import View, CreateView, DetailView, UpdateView, DeleteView
from .forms import PlateCreateForm, PlateSearchForm
from .models import Plate
from .tasks import execute_save

class PlateObjectMixin(object):
	model = Plate
	lookup = 'id'

	def get_object(self):
		id_ = self.kwargs.get(self.lookup)
		obj = None

		if id is not None:
			obj = get_object_or_404(Plate, id=id_)

		return obj

	def form_valid(self, form):
		execute_save.delay(form.cleaned_data)
		return super().form_valid(form)

# General main page for the plates database
class PlatesHomeView(View):
	form_class = PlateSearchForm

	def get(self, request, *args, **kwargs):
		return render(request, 'plates/plates_main.html', {})

	# Search function
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

class PlatesCreateView(PlateObjectMixin, CreateView):
	form_class = PlateCreateForm
	template_name = "plates/plates_create.html"

class PlatesDetailView(PlateObjectMixin, DetailView):
	template_name = "plates/plates_detail.html"
	queryset = Plate.objects.all()

class PlatesUpdateView(PlateObjectMixin, UpdateView):
	form_class = PlateCreateForm
	template_name = "plates/plates_update.html"
	queryset = Plate.objects.all()

class PlatesDeleteView(PlateObjectMixin, DeleteView):
	template_name = "plates/plates_delete.html"
	def get_success_url(self):

		return reverse ('plates:plates-list')
