from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from employees.models import Employee
from projects.models import Project
from tasks.models import Task
from attendance.models import Attendance
from leaveapp.models import LeaveRequest

@login_required
def dashboard(request):
    context = {
        "employee_count": Employee.objects.count(),
        "project_count": Project.objects.count(),
        "task_count": Task.objects.count(),
        "pending_tasks": Task.objects.filter(status="Pending").count(),
        "attendance_count": Attendance.objects.count(),
        "leave_count": LeaveRequest.objects.filter(status="Pending").count(),
        "recent_tasks": Task.objects.select_related("assigned_to", "project").order_by("-created_at")[:6],
        "recent_projects": Project.objects.order_by("-created_at")[:5],
    }
    return render(request, "dashboard.html", context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
