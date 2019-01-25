from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import PlantFamily, PlantSpecies
from .forms import *


def plant_species_home(request):
	families = PlantFamily.objects.prefetch_related('species').exclude(species=None)
	uncategorised_species = PlantSpecies.objects.filter(family__isnull=True)
	families = list(families)+list(uncategorised_species)
	context = {
		'page_title': 'Plant catalogue',
		'families': families,
	}
	return render(request, 'plants/home.html', context)


def plant_species_view(request, species_id):
	species = PlantSpecies.objects.get(pk=species_id)
	context = {
		'page_title': "Species: {}".format(species),
		'species': species,
	}
	return render(request, 'plants/species_view.html', context)


def plant_species_add(request):
	context = {
		'page_title': 'Add a plant species',
		'form': PlantSpeciesForm(),
	}
	if request.method == "POST":
		form = PlantSpeciesForm(request.POST)
		if form.is_valid():
			new_plant = form.save()
			#TODO: vvv Move this to the form's save method vvv
			user_group = request.user.groups.first()
			new_plant.user_group = user_group
			new_plant.save()
			return redirect('plant_species_home')
		else:
			context['form'] = form
	return render(request, 'plants/species_form.html', context)

	
def plant_species_edit(request, species_id):
	species = PlantSpecies.objects.get(pk=species_id)
	context = {
		'page_title': 'Edit {}'.format(species),
		'form': PlantSpeciesForm(instance=species),
	}
	if request.method == "POST":
		form = PlantSpeciesForm(request.POST, instance=species)
		if form.is_valid():
			plant = form.save()
			return redirect('plant_species_view', species_id)
		else:
			context['form'] = form
	return render(request, 'plants/species_form.html', context)
	

def plant_species_delete(request, species_id):
	species = PlantSpecies.objects.get(pk=species_id)
	name = species.name
	species.delete()
	messages.add_message(request, messages.INFO, '{} deleted'.format(name))
	return redirect('plant_species_home')


def plant_source_list(request):
	context = {
		'page_title': 'Plant sources',
		'sources': PlantSource.objects.all(),
	}
	return render(request, 'plants/source_list.html', context)


def plant_source_view(request, source_id):
	source = PlantSource.objects.get(pk=source_id)
	context = {
		'page_title': "Source: {}".format(source),
		'species': species,
	}
	return render(request, 'plants/species_view.html', context)


def plant_source_add(request):
	context = {
		'page_title': 'Add a source/supplier of plants',
		'form': PlantSourceForm(),
	}
	if request.method == "POST":
		form = PlantSourceForm(request.POST)
		if form.is_valid():
			new_plant = form.save()
			return redirect('plant_source_list')
		else:
			context['form'] = form
	return render(request, 'plants/species_form.html', context)

	
def plant_source_edit(request, source_id):
	source = PlantSource.objects.get(pk=source_id)
	context = {
		'page_title': 'Edit {}'.format(species),
		'form': PlantSourceForm(instance=source),
	}
	if request.method == "POST":
		form = PlantSourceForm(request.POST, instance=source)
		if form.is_valid():
			source = form.save()
			return redirect('plant_source_view', source_id)
		else:
			context['form'] = form
	return render(request, 'plants/source_form.html', context)
	

def plant_source_delete(request, source_id):
	source = PlantSource.objects.get(pk=source_id)
	name = source.name
	source.delete()
	messages.add_message(request, messages.INFO, '{} deleted'.format(name))
	return redirect('plant_species_home')




