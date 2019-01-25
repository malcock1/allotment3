from calendar import monthrange
from datetime import datetime

from django.shortcuts import render

from .models import Month
from plants.models import PlantSpecies

def month_view(request, month_id):
    months = Month.objects.all()
    month = months.get(pk=month_id)
    today = datetime.now().date()
    days_in_month = monthrange(today.year, int(month_id))
    tasks = {
                'seed_indoors': month.plants_to_seed_indoors.all(),
                'seed_outdoors': month.plants_to_seed_outdoors.all(),
                'plant_out': month.plants_to_plant_out.all(),
                'harvest': month.plants_to_harvest.all(),
            }
    context = {
        'page_title': "{} planner".format(month.name),
        'months': months,
        'month': month,
        'days_in_month': range(*days_in_month),
        'tasks': tasks,
    }
    return render(request, 'planner/month_view.html', context)


def year_view(request):
    """
    View the schedule for all plant species
    """
    # TODO: Add a filter to show only plants that exist (ie not the whole catalogue)
    months = Month.objects.all()
    plant_species = PlantSpecies.objects.filter(user_group__in=request.user.groups.all())
    context = {
        'months': months,
        'plant_species': plant_species,
    }
    return render(request, 'planner/year_view.html', context)
