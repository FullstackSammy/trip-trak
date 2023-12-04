from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Trip, Note

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
    
class TripDetailView(DetailView):
    model = Trip
    
    # Som det är nu så kommer vi bara få den datan som finns i Trip model. Men vi vill också ha med notes. För att kunna få med det så måste vi overrida context-variabeln som skickas med denna. Då gör vi så här:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context
    # med detta ovan så kommer vi ha access till den nya context-variabeln, vilket är våran Notes model.

class NoteDetailView(DetailView):
    model = Note
    
class NoteListView(ListView):
    model = Note
    
    # Overriding method for getting notes specific to a user.
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset

class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    
    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
    
class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    
    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
    
    
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    # no template needed - send a post request to this url


class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')