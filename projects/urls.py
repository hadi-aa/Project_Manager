from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('project/<str:project_pk>/', views.project, name='project'),
    path('create_project/', views.create_project, name='create_project'),
    path('update_project/<str:project_pk>/', views.update_project, name='update_project'),
    path('delete_project/<str:project_pk>/', views.delete_project, name='delete_project'),
]
