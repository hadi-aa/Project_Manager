from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project


def all_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/all_projects.html', context)


def project(request, project_pk):
    project_object = Project.objects.get(id=project_pk)
    return render(request, 'projects/project.html', {'project_object': project_object})


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            created_project = form.save()
            created_project
            return redirect('projects:project', created_project.id)
    return render(request, 'projects/project_form.html', {'form': form})


def update_project(request, project_pk):
    project_object = Project.objects.get(id=project_pk)
    form = ProjectForm(instance=project_object)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_object)
        if form.is_valid():
            updated_project = form.save()
            updated_project
            return redirect('projects:project', updated_project.id)
    return render(request, 'projects/project_form.html', {'form': form})


def delete_project(request, project_pk):
    project_object = Project.objects.get(id=project_pk)
    if request.method == 'POST':
        project_object.delete()
        return redirect('projects:all_projects')
    return render(request, 'delete.html', {'object': project_object})
