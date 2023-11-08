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
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from . import views



urlpatterns = [
    #Proyectos
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('register/', views.registerEmail, name='register'),
    path('projectsList/', views.projectsList, name='projectsList'),
    path('projectUpdate/<int:pk>/', login_required(views.ProjectUpdateView.as_view()), name='projectUpdate'),
    path('projects/create/', login_required(views.ProjectCreateView.as_view()), name='projectCreate'),
    path('projectRead/<int:pk>/', views.projectRead, name='projectRead'),
    path('projectQuestions/<int:pk>/', views.projectQuestions, name='projectQuestions'),
    path('projectCharts/', views.projectCharts, name='projectCharts'),
    path('policiesList/<int:projectId>/', views.policiesList, name='policiesList'),
    #Documentos
    #path('textUpdate/<int:pk>/', views.TextUpdateView.as_view(), name='textUpdate'),
    path('textProjectPolicyUpdate/<int:pk>/', login_required(views.TextProjectPolicyUpdateView.as_view()), name='textProjectPolicyUpdate'),
    #Usuarios
    path('logout/', views.exit, name='exit'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    path('activationSuccess/', views.activationSuccess, name='activationSuccess'),
    path('activationFailure/', views.activationFailure, name='activationFailure'),
    path('registrationSuccess/', views.registrationSuccess, name='registrationSuccess'),
    path('activationInvalid/', views.activationInvalid, name='activationInvalid'),
    path('accessDenied/', views.accessDenied, name='accessDenied'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    re_path(r'^(?!accounts/login/|admin).*$', views.pageNotFound),
]