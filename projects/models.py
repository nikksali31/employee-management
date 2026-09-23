from django.db import models
from employees.models import Employee
class Project(models.Model):
    STATUS=[("Planning","Planning"),("Active","Active"),("Completed","Completed"),("On Hold","On Hold")]
    name=models.CharField(max_length=150)
    description=models.TextField()
    client_name=models.CharField(max_length=120,blank=True)
    manager=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20,choices=STATUS,default="Planning")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
