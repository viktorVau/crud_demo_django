from django.urls import path
from .import views

urlpatterns = [
    path("home", views.home, name="myhome"),
    path("index", views.index, name="myindex"),
    path("about", views.about, name="aboutpage"),
    path("another", views.another, name="otherpage"),
    path("info", views.info, name="myinfo")
]