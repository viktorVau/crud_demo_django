from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

name = "Feranmi O Easy"

list1 = ["Python", "Java", "Javascript", "PHP", "Swift", "Django"]

blog = [
    {
        "title":"try me",
        "content":"try me in web arena",
        "author":"peter"
    },

    {
        "title":"try me",
        "content":"try me in web arena second time",
    },

    {
        "title":"try me",
        "content":"try me in web arena last time",
        "author":"peter"
    },

    {
        "title":"try me",
        "content":"this is python app",
        "author":"feranmi"
    },
]

def home(request):
    return render(request, "home.html", {"myname": name, "mylist": list1, "myblog":blog})
    # return HttpResponse("<h1> Hello Feranmi </h1>")

# def index(request):
#     return HttpResponse("<h1> Hello, Welcome to index page </h1>")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def another(request):
    return redirect("myindex")



def info(request):

    name = request.POST["myname"]
    age = request.POST["myage"]
    tech = request.POST["tech"]
    gender = request.POST["gender"]
    city = request.POST["city"]

    status = ""

    if gender == "m":
        status = "boy"
    else:
        status = "girl"

    details = f"My name is {name}, I am {age} years old, I am learning {tech}, I am a {status}, I came from {city}"
    return render(request, "index.html", {"mydetail":details})
