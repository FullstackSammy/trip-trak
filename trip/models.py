from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model() # Gets the user model. So now you can use this variable inside the model.

# Create your models here.

# Trips & Notes  model

class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True) # this means that it is not a required field. It is okay to store blank values.
    end_date = models.DateField(blank=True, null=True) # this means that it is not a required field. It is okay to store blank values.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips') # Foreign key, för det är many-to-one relationship. on_delete finns där för att radera alla trips om user blir deletat. relaterat namn 'trips', för att göra det åtkomligt i notes-modellen sen
    
    def __str__(self):
        return self.city
    

class Note(models.Model):
    # Choices for the type field
    EXCURSIONS = (
        ('event', 'Event'),
        ('dining', 'Dining'),
        ('experience', 'Experience'),
        ('general', 'General'),
    )
    
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes') # om en trip raderas så raderas alla notes som är associerat med den.
    name = models.CharField(max_length=100)
    decription = models.TextField()
    type = models.CharField(max_length=100, choices=EXCURSIONS)
    img = models.ImageField(upload_to='notes', blank=True, null=True) #blank and null means that uploading an image is not required.
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)]) # The validator is saying and doing so that you cannot put in a rating higher than 5.
    
    def __str__(self):
        return f"{self.name} in {self.trip.city}"
    