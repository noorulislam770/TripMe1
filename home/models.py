from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    response = models.TextField()
    date = models.DateField()
    def __str__(self) :
        return self.name
    

class User(models.Model):
    name = models.CharField(max_length=122)
    user_id = models.IntegerField()
    mobile = models.CharField(max_length=25)
    password = models.CharField(max_length=122)
    travel_history = models.CharField(max_length=122)
    reviews = models.CharField(max_length=250)
    def __str__(self) :
        return self.name

class TouristSpot(models.Model):
    name = models.CharField(max_length=122)
    spot_id = models.IntegerField()
    location = models.CharField(max_length=25)
    current_weather = models.CharField(max_length=122)
    current_road_conditions = models.CharField(max_length=122)
    reviews = models.CharField(max_length=250)
    hotel_services = models.CharField(max_length=250)
    car_rentals = models.CharField(max_length=250)
    def __str__(self) :
            return self.name
    
    
class Hotel(models.Model):
    name = models.CharField(max_length=122)
    hotel_id = models.IntegerField()
    hotel_contact = models.CharField(max_length=25)
    hotel_reviews = models.CharField(max_length=122)
    def __str__(self) :
            return self.name

class Event(models.Model):
    name = models.CharField(max_length=50)
    event_id = models.IntegerField()
    event_description = models.CharField(max_length=200)
    event_duration = models.CharField(max_length=50)
    reviews = models.CharField(max_length=200)
    def __str__(self) :
            return self.name
    
class Transportation(models.Model):
    name = models.CharField(max_length=50)
    transportation_id  = models.IntegerField()
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    name = models.IntegerField()
    def __str__(self) :
        return self.name
    
class Feedback(models.Model):
    Feedback_id = models.IntegerField()
    description = models.CharField(max_length=200)
    rating = models.IntegerField()
    date = models.DateField()
    def __str__(self) :
            return self.description
    

class TravelAgent(models.Model):
    agent_id = models.IntegerField()
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    email = models.CharField(max_length=70)

    def __str__(self) :
            return self.name



      