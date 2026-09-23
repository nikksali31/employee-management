from django.urls import path
from .views import *
urlpatterns=[path("",project_list,name="project_list"),path("add/",project_create,name="project_create"),path("<int:pk>/edit/",project_update,name="project_update"),path("<int:pk>/delete/",project_delete,name="project_delete")]
