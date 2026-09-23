from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import Task
from .forms import TaskForm
@login_required
def task_list(request):
    q=request.GET.get("q","")
    tasks=Task.objects.select_related("project","assigned_to").filter(title__icontains=q) if q else Task.objects.select_related("project","assigned_to").all()
    return render(request,"tasks/list.html",{"tasks":tasks,"q":q})
@login_required
def task_create(request):
    form=TaskForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("task_list")
    return render(request,"form.html",{"form":form,"title":"Add Task","back":"task_list"})
@login_required
def task_update(request,pk):
    obj=get_object_or_404(Task,pk=pk); form=TaskForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); return redirect("task_list")
    return render(request,"form.html",{"form":form,"title":"Edit Task","back":"task_list"})
@login_required
def task_delete(request,pk):
    obj=get_object_or_404(Task,pk=pk)
    if request.method=="POST": obj.delete(); return redirect("task_list")
    return render(request,"confirm_delete.html",{"object":obj,"back":"task_list"})
