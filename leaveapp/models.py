from django.db import models
from employees.models import Employee
class LeaveRequest(models.Model):
    STATUS=[("Pending","Pending"),("Approved","Approved"),("Rejected","Rejected")]
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS,default="Pending")
    applied_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.employee} - {self.status}"
