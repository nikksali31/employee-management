from django.db import models
from employees.models import Employee
from projects.models import Project
class Task(models.Model):
    PRIORITY=[("Low","Low"),("Medium","Medium"),("High","High"),("Urgent","Urgent")]
    STATUS=[("Pending","Pending"),("In Progress","In Progress"),("Completed","Completed")]
    title=models.CharField(max_length=180)
    description=models.TextField(blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    priority=models.CharField(max_length=10,choices=PRIORITY,default="Medium")
    status=models.CharField(max_length=20,choices=STATUS,default="Pending")
    due_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
