from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Destination
from django.shortcuts import get_object_or_404
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})
def about(request):
    print("welcome")
    return render(request, "org/about.html")
def contact(request):
    print("Welcome ")
    return render(request, "org/contact.html")
def news(request):
    print("Welcome ")
    return render(request, "org/news.html")
def destination(request):
    dests = Destination.objects.all()
    return render(request, "org/destinations.html")
def search(request):
    dests = Destination.objects.all()
    if dests.name == id:
        return render(request, "org/destinations.html")
    else:
        print("Destination does not exists")
    return render(request, "org/destinations.html")

