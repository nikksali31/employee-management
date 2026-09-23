from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import Attendance
from .forms import AttendanceForm
@login_required
def attendance_list(request): return render(request,"attendance/list.html",{"records":Attendance.objects.select_related("employee").order_by("-date")})
@login_required
def attendance_create(request):
    form=AttendanceForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("attendance_list")
    return render(request,"form.html",{"form":form,"title":"Add Attendance","back":"attendance_list"})
@login_required
def attendance_update(request,pk):
    obj=get_object_or_404(Attendance,pk=pk); form=AttendanceForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); return redirect("attendance_list")
    return render(request,"form.html",{"form":form,"title":"Edit Attendance","back":"attendance_list"})
@login_required
def attendance_delete(request,pk):
    obj=get_object_or_404(Attendance,pk=pk)
    if request.method=="POST": obj.delete(); return redirect("attendance_list")
    return render(request,"confirm_delete.html",{"object":obj,"back":"attendance_list"})
