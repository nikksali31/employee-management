from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class Employee(models.Model):
    DESIGNATIONS = [
        ("Developer","Developer"),("Designer","Designer"),("HR","HR"),
        ("Manager","Manager"),("Intern","Intern"),("QA","QA")
    ]
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=30, choices=DESIGNATIONS, default="Intern")
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    profile_image = models.ImageField(upload_to="employees/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.employee_id} - {self.name}"
