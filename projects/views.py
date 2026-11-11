from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Department, Project
from .forms import ProjectForm


# ---------- Public views ----------

def home(request):
    dept = get_object_or_404(Department, id=1)
    return render(request, "projects/home.html", {
        "message": "Welcome to the Student Project Management System!",
        "dept": dept,
    })


def department_projects(request, dept_name):
    projects = Project.objects.filter(department__name=dept_name)
    return render(request, "projects/list.html", {"projects": projects})


def project_list(request):
    query = request.GET.get("q", "")
    if query:
        projects = Project.objects.filter(title__icontains=query)
    else:
        projects = Project.objects.all()
    return render(request, "projects/project_list.html", {
        "projects": projects,
        "query": query,
    })


# ---------- Protected CRUD views ----------

@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/project_form.html", {"form": form, "action": "Add"})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "projects/project_form.html", {"form": form, "action": "Edit"})


@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    return render(request, "projects/project_confirm_delete.html", {"project": project})