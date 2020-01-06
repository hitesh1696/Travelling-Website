from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact),
    path("about", views.about),
    path("news", views.news),
    path("search", views.search),
    path("destination", views.destination, name="destinations"),


]

