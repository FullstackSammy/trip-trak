from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'