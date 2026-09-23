from django.urls import path
from .views import *
urlpatterns=[
 path("",employee_list,name="employee_list"), path("add/",employee_create,name="employee_create"),
 path("<int:pk>/edit/",employee_update,name="employee_update"), path("<int:pk>/delete/",employee_delete,name="employee_delete"),
 path("departments/",department_list,name="department_list"), path("departments/add/",department_create,name="department_create"),
 path("departments/<int:pk>/edit/",department_update,name="department_update"), path("departments/<int:pk>/delete/",department_delete,name="department_delete"),
]
