from django import forms
from django.forms import ModelForm

from .models import PlantSpecies, \
					Plant, \
					PlantSource

class PlantSpeciesForm(ModelForm):
	class Meta:
		model = PlantSpecies
		exclude = ('companions','user_group',)

	def __init__(self, *args, **kwargs):
		super(PlantSpeciesForm, self).__init__(*args, **kwargs)
		self.fields['water'].widget.attrs.update(**{'min':1,'max':5})

class PlantSourceForm(ModelForm):
	class Meta:
		model = PlantSource
		exclude = ()
