from django.shortcuts import render
from .models import Event

# Create your views here.

def list_events(request):
    events = Event.objects.all()
    context = {
        "events": events
    }

    return render(request, 'events/list.html', context)
