from django.urls import path
from .import views

urlpatterns = [
    path("employeeform", views.employee_form, name="employee_form"),
    path("employeeinfo", views.employee_info, name="employee_info"),
    path("removeemployee/<int:id>", views.remove_employee, name="removeemployee"),
    path("editemployee/<int:id>", views.update_employee, name="editemployee"),
]