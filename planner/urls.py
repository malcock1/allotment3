from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', year_view, name='year_view'),
    url(r'^month/(?P<month_id>[0-9]+)/$', month_view, name='month_view'),
]