from django.urls import path
from .views import *
urlpatterns=[path("",leave_list,name="leave_list"),path("add/",leave_create,name="leave_create"),path("<int:pk>/edit/",leave_update,name="leave_update"),path("<int:pk>/delete/",leave_delete,name="leave_delete")]
