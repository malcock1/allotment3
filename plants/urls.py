from django.conf.urls import url
import plants
from .views import *

urlpatterns = [
    url(r'^$', plant_species_home, name='plant_species_home'),
    url(r'^species/(?P<species_id>[0-9]+)/$', plant_species_view, name='plant_species_view'),
    url(r'^species/add/$', plant_species_add, name='plant_species_add'),
    url(r'^species/edit/(?P<species_id>[0-9]+)/$', plant_species_edit, name='plant_species_edit'),
    url(r'^species/delete/(?P<species_id>[0-9]+)/$', plant_species_delete, name='plant_species_delete'),
    url(r'^sources/$', plant_source_list, name='plant_source_list'),
    url(r'^sources/(?P<source_id>[0-9]+)/$', plant_source_view, name='plant_source_view'),
    url(r'^sources/add/$', plant_source_add, name='plant_source_add'),
    url(r'^sources/edit/(?P<source_id>[0-9]+)/$', plant_source_edit, name='plant_source_edit'),
    url(r'^sources/delete/(?P<source_id>[0-9]+)/$', plant_source_delete, name='plant_source_delete'),
]