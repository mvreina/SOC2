"""
URL configuration for soc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home, projects, projectsList, ProjectCreateView, ProjectUpdateView, projectRead, projectQuestions, exit, register
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('projectsList/', projectsList, name='projectsList'),
    path('projectUpdate/<int:pk>/', login_required(ProjectUpdateView.as_view()), name='projectUpdate'),
    path('projects/create/', login_required(ProjectCreateView.as_view()), name='projectCreate'),
    path('projectRead/<int:pk>/', projectRead, name='projectRead'),
    path('projectQuestions/<int:pk>/', projectQuestions, name='projectQuestions'),
    #path('projectQuestionsUpdate/<int:pk>/', login_required(ProjectQuestionUpdateView.as_view()), name='projectQuestionsUpdate'),
]