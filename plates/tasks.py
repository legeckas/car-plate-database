from carplates.celery import app
from .forms import PlateCreateForm

@app.task
def execute_save(plate_data):
	form = PlateCreateForm(plate_data)
	
	if form.is_valid():
		form.save()