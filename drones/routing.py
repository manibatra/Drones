from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/drones/stimulator/$', consumers.DroneConsumer),
    url(r'^ws/drones/dashboard/$', consumers.DashboardConsumer),

]