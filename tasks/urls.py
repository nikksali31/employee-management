from django.urls import path
from .views import *
urlpatterns=[path("",task_list,name="task_list"),path("add/",task_create,name="task_create"),path("<int:pk>/edit/",task_update,name="task_update"),path("<int:pk>/delete/",task_delete,name="task_delete")]
