from django.shortcuts import render

from .models import Student

# Create your views here.

def student_form(request):
    if request.method == "POST":
        name = request.POST("name")
        age = request.POST("age")
        gender = request.POST("gender")
        email = request.POST("email")

        new_student = Student(name = name, age = age, gender = gender, email = email)
        new_student.save()

    return render(request,'student.html')