from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import LeaveRequest
from .forms import LeaveRequestForm
@login_required
def leave_list(request): return render(request,"leave/list.html",{"leaves":LeaveRequest.objects.select_related("employee").order_by("-applied_at")})
@login_required
def leave_create(request):
    form=LeaveRequestForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("leave_list")
    return render(request,"form.html",{"form":form,"title":"Apply Leave","back":"leave_list"})
@login_required
def leave_update(request,pk):
    obj=get_object_or_404(LeaveRequest,pk=pk); form=LeaveRequestForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); return redirect("leave_list")
    return render(request,"form.html",{"form":form,"title":"Edit Leave Request","back":"leave_list"})
@login_required
def leave_delete(request,pk):
    obj=get_object_or_404(LeaveRequest,pk=pk)
    if request.method=="POST": obj.delete(); return redirect("leave_list")
    return render(request,"confirm_delete.html",{"object":obj,"back":"leave_list"})
