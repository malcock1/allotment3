from datetime import datetime
from random import randint

from django.shortcuts import render

from planner.models import Month
from plants.models import Plant, PlantSpecies

def dashboard(request):
	month = Month.objects.get(pk=datetime.now().month)
	month_tasks = {
		'Seed indoors': month.plants_to_seed_indoors.all().values_list('name', flat=True),
		'Seed outdoors': month.plants_to_seed_outdoors.all().values_list('name', flat=True),
		'Plant out': month.plants_to_plant_out.all().values_list('name', flat=True),
		'Harvest': month.plants_to_harvest.all().values_list('name', flat=True),
	}
	month_tasks_tidy = {k:(month_tasks[k]) for k in month_tasks if month_tasks[k]}
	context = {
		'page_title': "Dashboard",
		'plant_count': Plant.objects.count(),
		'month_tasks': month_tasks_tidy,
		'principle': "dashboard/principle_{}.gif".format(str(randint(1,12))),
	}
	return render(request, 'dashboard/dashboard.html', context)
