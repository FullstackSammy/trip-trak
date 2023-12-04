from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

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

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    # Looking for template named model_form.html dvs trip_form
    
    def form_valid(self, form):
        # owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)