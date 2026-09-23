from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm

@login_required
def employee_list(request):
    q=request.GET.get("q","")
    employees=Employee.objects.select_related("department").filter(name__icontains=q) if q else Employee.objects.select_related("department").all()
    return render(request,"employees/list.html",{"employees":employees,"q":q})

@login_required
def employee_create(request):
    form=EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid(): form.save(); return redirect("employee_list")
    return render(request,"form.html",{"form":form,"title":"Add Employee","back":"employee_list"})

@login_required
def employee_update(request,pk):
    obj=get_object_or_404(Employee,pk=pk); form=EmployeeForm(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid(): form.save(); return redirect("employee_list")
    return render(request,"form.html",{"form":form,"title":"Edit Employee","back":"employee_list"})

@login_required
def employee_delete(request,pk):
    obj=get_object_or_404(Employee,pk=pk)
    if request.method=="POST": obj.delete(); return redirect("employee_list")
    return render(request,"confirm_delete.html",{"object":obj,"back":"employee_list"})

@login_required
def department_list(request):
    return render(request,"departments/list.html",{"departments":Department.objects.all()})

@login_required
def department_create(request):
    form=DepartmentForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("department_list")
    return render(request,"form.html",{"form":form,"title":"Add Department","back":"department_list"})

@login_required
def department_update(request,pk):
    obj=get_object_or_404(Department,pk=pk); form=DepartmentForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); return redirect("department_list")
    return render(request,"form.html",{"form":form,"title":"Edit Department","back":"department_list"})

@login_required
def department_delete(request,pk):
    obj=get_object_or_404(Department,pk=pk)
    if request.method=="POST": obj.delete(); return redirect("department_list")
    return render(request,"confirm_delete.html",{"object":obj,"back":"department_list"})
