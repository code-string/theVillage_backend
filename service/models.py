from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    service_image = CloudinaryField('service_image', blank=True)
    

    def __str__(self):
        return self.title



class TeamMember(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    team_image = CloudinaryField('team_image', blank=True)

    def __str__(self):
        return self.title



class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    events_image = CloudinaryField('events_image', blank=True)


    def __str__(self):
        return self.title


class HappyClients(models.Model):
    name = models.CharField(max_length=100)
    client_image = CloudinaryField('client_image', blank=True)

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    about_image = CloudinaryField('about_image', blank=True)
    description = models.TextField()
    mission = models.TextField()
    mission_image = models.ImageField('mission_image', blank=True)
    visions = models.TextField()
    visions_image = CloudinaryField('vissions_image', blank=True)
    value1 = models.CharField(max_length=150)
    value2 = models.CharField(max_length=150)
    value3 = models.CharField(max_length=150, blank=True)
    value4 = models.CharField(max_length=150, blank=True)
    value_image = CloudinaryField('value_image', blank=True)
    twitter = models.URLField(max_length=250, blank=True)
    instangram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Segmentation(models.Model):
    title = models.CharField(max_length=100)
    seg_image = models.ImageField(blank=True)
    description = models.TextField()

    def __str__ (self):
        return self.title


class ContactUs(models.Model):
    fullname = models.CharField(max_length=150,)
    phone_regex = RegexValidator(regex=r'^[0]\d{10}$',message="must be a valid phone number")
    phone = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    email = models.EmailField(max_length=200)
    comment = models.TextField(blank=True, null=True)