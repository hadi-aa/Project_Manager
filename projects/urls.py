from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
   path('', views.all_project, name='all_project'),
   path('project/<str:project_pk>/', views.projects, name='project'),
]
