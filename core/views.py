from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .user import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Project, Answer, Question, ProjectQuestion
from django.http import  JsonResponse
#from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView
from .forms import ProjectForm, AnswerForm, QuestionForm, ProjectQuestionForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import math

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

# PROYECTOS
@login_required
def projects(request):
    # projectsList = Project.objects.all()
    # projectsList = Project.objects.all().order_by('name')
    # return render(request, 'core/projects.html' , {'projects': projectsList})
    return render(request, 'core/projects.html')

# Usado para construir la DataTable en la vista de lista
@login_required
def projectsList(request):
    # Filter by Current User
    projectsUser = Project.objects.filter(createdBy=request.user)
    projects = list(projectsUser.values())
    data = {'projects': projects}
    return JsonResponse(data)

# Ver proyecto
@login_required
def projectRead(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'core/projectRead.html', {'project': project})

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'core/projectUpdate.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        # Set the author to the currently logged-in user
        form.instance.createdBy = self.request.user
        messages.success(self.request, 'Proyecto actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar proyecto.')
        return self.render_to_response(self.get_context_data(form=form))
    


# Crear proyecto
class ProjectCreateView(CreateView):

    model = Project
    form_class = ProjectForm
    template_name = 'core/projectCreate.html'
    success_url = reverse_lazy('projectQuestions')

    def form_valid(self, form):
        # Set the author to the currently logged-in user
        form.instance.createdBy = self.request.user
        project = form.save()
        #self.success_url = '/projectQuestions/' + str(project.id)
        self.success_url = reverse('projectQuestions', kwargs={'pk': project.id})
        # Create questions
        self.createQuestions(project)
        #messages.success(self.request, 'Proyecto creado correctamente.')   
        return super().form_valid(form) 

    def form_invalid(self, form):
        messages.warning(self.request, 'No se guardó el proyecto.')
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))




    
    # Create ProjectQuestion - Relation to Project Question and Answer
    def createQuestions(self, project):
        questions = Question.objects.all()
        for question in questions:
            answers = Answer.objects.filter(question=question)
            for answer in answers:
                if answer.type == 'checkbox':
                    userAnswer = True
                else:
                    userAnswer = False
                # Create ProjectQuestion
                projectQuestion = ProjectQuestion.objects.create(project=project, userAnswer=userAnswer, orderProjectQuestion=answer.orderAnswer)
                projectQuestion.question.add(question)
                projectQuestion.answer.add(answer)

# PREGUNTAS
class QuestionCreateView(CreateView):
    model = Question


# RESPUESTAS
class AnswerCreateView(CreateView):
    model = Answer

# PROYECTO - PREGUNTAS - RESPUESTAS
@login_required
def projectQuestions(request, pk):
    try:
        project = Project.objects.get(id=pk)
        question = Question.objects.get(orderQuestion=project.numQuestion)
        answers = Answer.objects.filter(question=question)
        totalQuestions = 13
        percentageProgress = math.ceil((project.numQuestion / totalQuestions) * 100)
        print("Pregunta actual:", project.numQuestion)

        if request.method == 'POST':
            #saveAnswers = request.POST.get("projectQuestions")
            #print(saveAnswers)
            projectQuestions = ProjectQuestion.objects.filter(project=project, question=question).order_by('orderProjectQuestion')
            pq_ids = []            
            #Guardar respuestas tipo checkbox
            if question.type == 'checkbox':
                print("Actualizando proyecto con preguntas tipo checkbox")
                for x in projectQuestions:
                    pq_ids.append(request.POST.get(str(x.id)))
                    #print(str(x.id))
                    #print(request.POST.get(str(x.id)))
                    if request.POST.get(str(x.id)) == None: 
                        x.userAnswer = False 
                    else: 
                        x.userAnswer = True
                    print("Se guardó correctamente el proyecto")
                    x.save()
            else:
                #Guardar respuestas tipo radio
                print("Actualizando proyecto con preguntas tipo radio")
                selected = request.POST.get('flexRadioDefault')
                print("selected", selected)
                print("Type", type(selected))
                #Si no ha seleccionado nada se muestra un mensaje de información y en la misma pregunta
                if selected == None:
                    messages.warning(request, "Por favor, selecciona una respuesta.")
                    context = {'projectQuestions': projectQuestions, 'question': question, 'percentageProgress': percentageProgress, 
                    'totalQuestions': totalQuestions, 'answers': answers, 'project': project}
                    return render(request, 'core/projectQuestions.html', context)
                else:
                    #Si seleccionó una respuesta se guarda
                    for x in projectQuestions:
                        pq_ids.append(request.POST.get(str(x.id)))
                        print(x.id)
                        print(type(x.id))
                        if str(x.id) == selected: 
                            x.userAnswer = True 
                        else: 
                            x.userAnswer = False
                        print("Se guardó correctamente el proyecto")
                        x.save()

            print("pq_ids", pq_ids)


            #Avanzar a la siguiente respuesta
            if 'finish' in request.POST:
                project.numQuestion += 1
                project.save()
                success_url = reverse('projectRead', kwargs={'pk': project.id})
                return redirect(success_url)
            elif 'next' in request.POST:
                
                project.numQuestion += 1
                project.save()
                question = Question.objects.get(orderQuestion=project.numQuestion)
                answers = Answer.objects.filter(question=question)
                projectQuestions = ProjectQuestion.objects.filter(project=project, question=question).order_by('orderProjectQuestion')
                percentageProgress = math.ceil((project.numQuestion / totalQuestions) * 100)
                print("Avanza a la pregunta: " + str(project.numQuestion))

            
            #if formProject.is_valid():
            #    formProject.save()

        else:
            #projectQuestions = ProjectQuestion.objects.filter(project=project, question=question)
            #projectQuestions = ProjectQuestionForm(initial={'project': project, 'question': question})
            projectQuestions = ProjectQuestion.objects.filter(project=project, question=question).order_by('orderProjectQuestion')

        #print(projectQuestions)
        #print(projectQuestions.first())
        #print(projectQuestions.first().answer.values()[0]['text'])
        #print(list(projectQuestions))
        #list_projectQuestion = list(projectQuestions)
        #for x in list_projectQuestion:
            #print(x.answer.values()[0]['text'])

        #for x in projectQuestions:
        #    print(x.answer.values()[0]['text'])
        #print(answers.values())
        context = {'projectQuestions': projectQuestions, 'question': question, 'percentageProgress': percentageProgress, 
                    'totalQuestions': totalQuestions, 'answers': answers, 'project': project}
        return render(request, 'core/projectQuestions.html', context)
      
    except Exception as e:
        messages.warning(request, "Se produjo una excepción, consulte al Administrador")
        print("Se produjo una excepción: "+str(e))
        return redirect('projects')

class ProjectListView(ListView):
    model = Project

class AnswerListView(ListView):
    model = Answer

class QuestionListView(ListView):
    model = Question

# Logout
def exit(request):
    logout(request)
    return redirect('home')

# User registration
def register(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )

            login(request, user)

            return redirect('home')
        else:
            data['form'] = user_creation_form
            return render(request, 'registration/register.html', data)


    return render(request, 'registration/register.html', data)
