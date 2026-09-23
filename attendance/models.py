from django.db import models
from employees.models import Employee
class Attendance(models.Model):
    STATUS=[("Present","Present"),("Absent","Absent"),("Late","Late"),("Leave","Leave")]
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=10,choices=STATUS,default="Present")
    check_in=models.TimeField(null=True,blank=True)
    check_out=models.TimeField(null=True,blank=True)
    notes=models.CharField(max_length=255,blank=True)
    class Meta: unique_together=("employee","date")
    def __str__(self): return f"{self.employee} - {self.date}"
