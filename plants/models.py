from django.db import models
from django.contrib.auth.models import Group

LIGHT_CHOICES = [
    (1,'Full shade'),
    (2,'Partial shade'),
    (3,'Shade tolerant'),
    (4,'Partial sun'),
    (5,'Full sun'),
]

MONTH_ACTIVITIES = ['seed_indoors','seed_outdoors','plant_out','harvest',]

class PlantSpecies(models.Model):
    name = models.CharField(max_length=128)
    latin_name = models.CharField(max_length=128, null=True, blank=True)
    family = models.ForeignKey("PlantFamily", null=True, blank=True, on_delete=models.SET_NULL, related_name="species")
    user_group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, related_name="plant_species")

    seed_indoors = models.ManyToManyField("planner.Month", related_name='plants_to_seed_indoors')
    seed_outdoors = models.ManyToManyField("planner.Month", related_name='plants_to_seed_outdoors')
    plant_out = models.ManyToManyField("planner.Month", related_name='plants_to_plant_out')
    harvest = models.ManyToManyField("planner.Month", related_name='plants_to_harvest')

    full_height = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Full height (cm)') # In centimeters
    full_diameter = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Full diameter (cm)') # In centimeters
    light = models.PositiveSmallIntegerField(choices=LIGHT_CHOICES, null=True, blank=True)
    water = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Watering requirements: 1 (drought tolerant) - 5 (needs regular watering)') # How much it needs from 1-5

    notes = models.TextField(null=True, blank=True)

    annual = models.BooleanField(default=False)

    companions = models.ManyToManyField("self", related_name='companions') # Species that go well together


    @property
    def dimensions_str(self):
        dimensions = []
        if self.full_height:
            dimensions.append("H: {}cm".format(self.full_height))
        if self.full_diameter:
            dimensions.append("D: {}cm".format(self.full_diameter))
        return " // ".join(dimensions) or None

    @property
    def annual_str(self):
        return 'Annual' if self.annual else 'Perennial'

    def __str__(self):
        if self.latin_name:
            return "{} ({})".format(self.name, self.latin_name)
        else:
            return self.name

    @property
    def month_matrix(self):
        from planner.models import MONTHS, Month
        d = {
            month_id: "" for month_id in MONTHS.keys()
        }
        dd = {
            activity: list(getattr(self, activity).values_list('id', flat=True)) for activity in MONTH_ACTIVITIES
        }
        months = Month.objects.all()
        for activity in dd:
            for month_id in dd[activity]:
                d[month_id]+="{} ".format(activity)
        return d



class PlantFamily(models.Model):
    name = models.CharField(max_length=32)
    """
    ['Root',
    'Mushroom',
    'Flower',
    'Allium',
    'Salad leaves',
    'Brassica',
    'Legume',
    'Vegetable',
    'Hard fruit',
    'Soft fruit',
    'Herb',
    'Nut',
    'Grain',
    'Non-edible']
    """
    def __str__(self):
        return self.name


class PlantAttribute(models.Model):
    pass
    """
    'Tree',
    'Climber',

    """

class PlantSource(models.Model):
    name = models.CharField(max_length=128)
    web_address = models.CharField(max_length=256)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Plant(models.Model):
    """ An instance of a real physical plant or seed """

    species = models.ForeignKey(PlantSpecies, on_delete=models.PROTECT, related_name="plants")
    bed = models.ForeignKey("designs.Bed", on_delete=models.CASCADE, null=True)

    # Could put harvested weight in here?
    source = models.ForeignKey(PlantSource, null=True, on_delete=models.SET_NULL)
    cost = models.PositiveSmallIntegerField() # In pence per plant/seed



class Harvest(models.Model):
    """
    When we harvest we can store some info about the plants,
    quantities, comments etc
    """
    plants = models.ManyToManyField(Plant)
    # Not sure about this bit, probably put it in too soon
    # Consider having M2M field for beds, plant species
