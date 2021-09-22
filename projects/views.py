from django.shortcuts import render


def all_project(request):
    return render(request, 'projects/all_projects.html')


def projects(request, project_pk):
    return render(request, 'projects/project.html')
