from django import forms
from .models import Plate

class PlateCreateForm(forms.ModelForm):
	plate_number 	= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter a plate number'}))
	first_name 		= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter a first name'}))
	last_name 		= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter a last name'}))
	class Meta:
		model 	= Plate
		fields 	= [
			'plate_number',
			'first_name',
			'last_name'
		]