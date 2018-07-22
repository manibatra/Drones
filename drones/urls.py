from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stimulator/$', views.stimulator, name='stimulator'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]