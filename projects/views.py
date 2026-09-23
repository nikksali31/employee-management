from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import Project
from .forms import ProjectForm
@login_required
def project_list(request):
    q=request.GET.get("q","")
    projects=Project.objects.select_related("manager").filter(name__icontains=q) if q else Project.objects.select_related("manager").all()
    return render(request,"projects/list.html",{"projects":projects,"q":q})
@login_required
def project_create(request):
    form=ProjectForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("project_list")
    return render(request,"form.html",{"form":form,"title":"Add Project","back":"project_list"})
@login_required
def project_update(request,pk):
    obj=get_object_or_404(Project,pk=pk); form=ProjectForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); return redirect("project_list")
    return render(request,"form.html",{"form":form,"title":"Edit Project","back":"project_list"})
@login_required
def project_delete(request,pk):
    obj=get_object_or_404(Project,pk=pk)
    if request.method=="POST": obj.delete(); return redirect("project_list")
    return render(request,"confirm_delete.html",{"object":obj,"back":"project_list"})
