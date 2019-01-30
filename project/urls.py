from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from project.healthcheck import health

import plants, planner, designs

from registration.views import exit_page, signup
from dashboard.views import dashboard

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^/$', dashboard, name='home'),
    url(r'^health$', health),
    url(r'^sign-up/$', signup, name='signup'),
    url(r'^plants/', include('plants.urls')),
    url(r'^planner/', include('planner.urls')),
    url(r'^designs/', include('designs.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
