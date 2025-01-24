from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "add.html")

def add(request):
    if request.method == 'POST':
        num1 = float(request.POST['val1'])
        num2 = float(request.POST['val1'])

        result = num1**2 + num2**2
        # result = num1 + num2

        return render(request, "myresult.html", {"answer":result})

