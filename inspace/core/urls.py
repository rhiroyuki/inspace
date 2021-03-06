from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^planet/$',
        views.planet_create_view,
        name='planet-create'),
    url(r'^resource/$',
        views.resource_create_view,
        name='resource-create'),
    url(r'^resourcelink/$',
        views.resource_link_create_view,
        name='resource-link-create'),
    url(r'^resources/',
        views.resources_view,
        name='resource-list'),
    url(r'^$',
        views.home_view,
        name='home'),
]
