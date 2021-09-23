from django.contrib import admin
from django.urls import path, include

from Project_Manager import views

app_name = 'Project_Manager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('projects/', include('projects.urls'))
]
