from django.shortcuts import redirect, render

from .models import Employee

# Create your views here.


def employee_form(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        age = request.POST['age']
        gender = request.POST['gender']
        salary = request.POST['salary']

        new_employee = Employee(first_name = first_name, last_name = last_name, age = age, gender = gender, salary = salary)
        new_employee.save()

        return redirect('employee_info')

    
    return render(request, 'employee.html')


def employee_info(request):
    all_employees = Employee.objects.all()
    return render(request, "employee_info.html", {'employees':all_employees})

def remove_employee(request, id):
    employee_to_remove = Employee.objects.get(pk = id)
    employee_to_remove.delete()

    return redirect("employee_info")


def update_employee(request, id):
     
     employee_to_edit = Employee.objects.get(pk = id)

     if request.method == "POST":
        employee_to_edit.first_name = request.POST['fname']
        employee_to_edit.last_name = request.POST['lname']
        employee_to_edit.age = request.POST['age']
        employee_to_edit.gender = request.POST['gender']
        employee_to_edit.salary = request.POST['salary']

        employee_to_edit.save()

        return redirect("employee_info")
     
     return render(request, "update_employee.html", {"latest_employee":employee_to_edit})