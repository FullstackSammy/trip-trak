from django.urls import reverse_lazy # Importera redirection för när man har skapat ett konto.
from django.views.generic import TemplateView, CreateView # Importerar views som vi ska ha när vi bygger våra egna.
from django.contrib.auth.forms import UserCreationForm # Importerar user creation form

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # When user successfully creates an account. Return them to login page to log in.
    template_name = 'registration/signup.html'