from django.shortcuts import render, redirect
from .models import Service, TeamMember, Event, HappyClients, AboutUs, Segmentation, ContactUs
from .forms import ContactUsForm

# Create your views here.

def index(request):
    services = Service.objects.all()
    teammembers = TeamMember.objects.all()
    clients = HappyClients.objects.all()

    context = {
        'services': services,
        'teamembers': teammembers,
        'clients': clients
    }

    return render(request, 'index.html', context)




def about(request):
    about_us = AboutUs.objects.all()
    segment = Segmentation.objects.all()
    context = {
        'abouts': about_us,
        'segments': segment
    }

    return render(request, 'about.html', context)


def contact_us(request):
    form = ContactUsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
    form = ContactUsForm()
    context = {
        'form': form
    }

    return render(request, 'contact_us.html', context)





