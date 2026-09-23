from django import forms
from .models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {"joining_date": forms.DateInput(attrs={"type":"date"})}

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
