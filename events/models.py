from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')
    start_date = models.DateTimeField(blank = True)
    end_date = models.DateTimeField(blank = True)
    



    def eventEnded(self, *args, **kwargs):
        if datetime.now() > self.end_date:
            return "Event has ended"
        else:
            return "Event is still available"


    def __str__(self):
        return self.title

    
    

