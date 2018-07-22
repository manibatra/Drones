from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'drones/index.html', {})


def stimulator(request):
	return render(request, 'drones/stimulator.html', {})
