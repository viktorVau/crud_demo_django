from django.urls import path

from .import views




urlpatterns = [
    path("studentform", views.student_form, name='studentform')
]