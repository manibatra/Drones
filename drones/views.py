from django.shortcuts import render
import os
import json

# Create your views here.
def index(request):
    return render(request, 'drones/index.html', {})


def stimulator(request):
	return render(request, 'drones/stimulator.html', {})


def dashboard(request):
	map_api_key = os.environ['MAP_KEY']
	return render(request, 'drones/dashboard.html', {
		'map_api_key' : map_api_key
		})
