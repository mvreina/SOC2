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
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.registerEmail, name='register'),
    path('projectsList/', views.projectsList, name='projectsList'),
    path('projectUpdate/<int:pk>/', login_required(views.ProjectUpdateView.as_view()), name='projectUpdate'),
    path('projects/create/', login_required(views.ProjectCreateView.as_view()), name='projectCreate'),
    path('projectRead/<int:pk>/', views.projectRead, name='projectRead'),
    path('projectQuestions/<int:pk>/', views.projectQuestions, name='projectQuestions'),
    #path('accounts/login/', views.login, name='login'),
    #path('projectQuestionsUpdate/<int:pk>/', login_required(ProjectQuestionUpdateView.as_view()), name='projectQuestionsUpdate'),
    #User Registration Email
    #path('register_email/', views.register_email, name='register_email'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    path('activationSuccess/', views.activationSuccess, name='activationSuccess'),
    path('activationFailure/', views.activationFailure, name='activationFailure'),
    path('registrationSuccess/', views.registrationSuccess, name='registrationSuccess'),
    path('activationInvalid/', views.activationInvalid, name='activationInvalid'),
    path('accessDenied/', views.accessDenied, name='accessDenied'),
    re_path(r'^(?!accounts/login/|admin).*$', views.pageNotFound),
]