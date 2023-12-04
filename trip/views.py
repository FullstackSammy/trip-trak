from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from .models import Trip

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'
    


def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips,
    }
    
    return render(request, 'trip/trips_list.html', context)