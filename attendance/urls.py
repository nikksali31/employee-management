from django.urls import path
from .views import *
urlpatterns=[path("",attendance_list,name="attendance_list"),path("add/",attendance_create,name="attendance_create"),path("<int:pk>/edit/",attendance_update,name="attendance_update"),path("<int:pk>/delete/",attendance_delete,name="attendance_delete")]
