from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .user import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Project, Answer, Question, ProjectQuestion, Policy, ProjectPolicy, Text, Control, ProjectControl
from django.http import  JsonResponse
#from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView
from .forms import ProjectForm, TextForm, TextProjectPolicyForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import math
from django.http import Http404
#User registration
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
#Activate
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str

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
    try:
        project = Project.objects.get(id=pk)

        # Check if the logged-in user is the owner of the resource
        if request.user == project.createdBy:
            # Allow access to the resource
            projectPolicies = ProjectPolicy.objects.filter(project=project).order_by('orderProjectPolicy')
            totalPolicies = 32
            excludedPolicies = [int(value) for value in project.excludedPolicies]
            #print(excludedPolicies)
            #print(len(excludedPolicies))
            progressPolicies = math.ceil(((totalPolicies - len(excludedPolicies)) / totalPolicies) * 100)
            projectControls = ProjectControl.objects.filter(project=project).order_by('orderProjectControl')
            totalControls = 409
            excludedControls = [int(value) for value in project.excludedControls]
            #print(excludedControls)
            #print(len(excludedControls))
            progressControls = math.ceil(((totalControls - len(excludedControls)) / totalControls) * 100)
            return render(request, 'core/projectRead.html', {'project': project, 'progressPolicies': progressPolicies, 'projectPolicies': projectPolicies, 'progressControls': progressControls, 'projectControls': projectControls})
        else:
            # Deny access
            raise Http404("Recurso no encontrado")
        
    except Project.DoesNotExist:
        raise Http404("recurso no encontrado")

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
        #print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    # Crear ProjectQuestion - Es la relación entre Proyecto y Preguntas y Respuestas
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
        #print("Pregunta actual:", project.numQuestion)

        if request.method == 'POST':
            #saveAnswers = request.POST.get("projectQuestions")
            #print(saveAnswers)
            projectQuestions = ProjectQuestion.objects.filter(project=project, question=question).order_by('orderProjectQuestion')
            projectQuestionId = []
            numSelected = 0 #Contador de respuestas seleccionadas    
            #Guardar respuestas tipo checkbox
            if question.type == 'checkbox':
                #print("Actualizando proyecto con preguntas tipo checkbox")
                for x in projectQuestions:
                    projectQuestionId.append(request.POST.get(str(x.id)))
                    #print(str(x.id))
                    #print(request.POST.get(str(x.id)))
                    if request.POST.get(str(x.id)) == None: 
                        x.userAnswer = False 
                    else: 
                        x.userAnswer = True
                        numSelected += 1
                        # Se excluyen la politicas dependiendo de las respuestas seleccionadas
                        #print("Respuesta tipo checkbox seleccionada política excluida:", x.answer.values()[0]['excludedPolicies'])
                        # Si la politica ya había sido excluida, no se vuelve agregar al proyecto
                        excludedPolicies = [int(value) for value in project.excludedPolicies]
                        answerExcludedPolicies = [int(value) for value in x.answer.values()[0]['excludedPolicies']]
                        #print(excludedPolicies)
                        #print(answerExcludedPolicies)
                        for expl in answerExcludedPolicies:
                            if not expl in excludedPolicies:
                                project.excludedPolicies += (expl,)
                                project.save()
                        # Si el control ya había sido excluido, no se vuelve agregar al proyecto
                        #print("Paso 1")
                        excludedControls = [int(value) for value in project.excludedControls]
                        #print("Paso 2")
                        answerExcludedControls = [int(value) for value in x.answer.values()[0]['excludedControls']]
                        #print(excludedControls)
                        #print("Paso 3")
                        #print(answerExcludedControls)
                        #print("Paso 4")
                        for excl in answerExcludedControls:
                            #print("Paso 5", excl)
                            if not excl in excludedControls:
                                #print("Paso 6", excl)
                                project.excludedControls += (excl,)
                                #print("Paso 7")
                                project.save()
                            #print("Paso 8")
                        #print("Paso 9")
                    x.save()
                    #print("Se guardó correctamente el proyectQuestion")
                #Si no ha seleccionado nada se muestra un mensaje de información y sigue en la misma pregunta
                if numSelected == 0:
                    messages.warning(request, "Por favor, seleccione una respuesta.")
                    context = {'projectQuestions': projectQuestions, 'question': question, 'percentageProgress': percentageProgress, 
                    'totalQuestions': totalQuestions, 'answers': answers, 'project': project}
                    return render(request, 'core/projectQuestions.html', context)
            else:
                #Guardar respuestas tipo radio
                #print("Actualizando proyecto con preguntas tipo radio")
                selected = request.POST.get('flexRadioDefault')
                #print("selected", selected)
                #print("Type", type(selected))
                #Si no ha seleccionado nada se muestra un mensaje de información y sigue en la misma pregunta
                if selected == None:
                    messages.warning(request, "Por favor, seleccione una respuesta.")
                    context = {'projectQuestions': projectQuestions, 'question': question, 'percentageProgress': percentageProgress, 
                    'totalQuestions': totalQuestions, 'answers': answers, 'project': project}
                    return render(request, 'core/projectQuestions.html', context)
                else:
                    #Si seleccionó una respuesta se guarda
                    for x in projectQuestions:
                        projectQuestionId.append(request.POST.get(str(x.id)))
                        #print(x.id)
                        #print(type(x.id))
                        if str(x.id) == selected: 
                            x.userAnswer = True
                            # Se excluyen la politicas dependiendo de las respuestas seleccionadas
                            #print("Respuesta tipo radio seleccionada política excluida:", x.answer.values()[0]['excludedPolicies'])
                            # Si la politica ya había sido excluida, no se vuelve agregar al proyecto
                            excludedPolicies = [int(value) for value in project.excludedPolicies]
                            answerExcludedPolicies = [int(value) for value in x.answer.values()[0]['excludedPolicies']]
                            #print(excludedPolicies)
                            #print(answerExcludedPolicies)
                            for expl in answerExcludedPolicies:
                                if not expl in excludedPolicies:
                                    project.excludedPolicies += (expl,)
                                    project.save()
                            # Si el control ya había sido excluido, no se vuelve agregar al proyecto
                            excludedControls = [int(value) for value in project.excludedControls]
                            answerExcludedControls = [int(value) for value in x.answer.values()[0]['excludedControls']]
                            #print(excludedControls)
                            #print(answerExcludedControls)
                            for excl in answerExcludedControls:
                                if not excl in excludedControls:
                                    project.excludedControls += (excl,)
                                    project.save()

                        else: 
                            x.userAnswer = False
                        #print("Se guardó correctamente el proyecto")
                        x.save()

            #print("projectQuestionId", projectQuestionId)


            #Avanzar a la siguiente respuesta
            if 'finish' in request.POST:
                project.numQuestion += 1
                project.save()
                # Crea las politicas y las asocia al proyecto
                createPolicies(project, request.user)
                createControls(project)
                success_url = reverse('projectRead', kwargs={'pk': project.id})
                return redirect(success_url)
            elif 'next' in request.POST:
                
                project.numQuestion += 1
                project.save()
                question = Question.objects.get(orderQuestion=project.numQuestion)
                answers = Answer.objects.filter(question=question)
                projectQuestions = ProjectQuestion.objects.filter(project=project, question=question).order_by('orderProjectQuestion')
                percentageProgress = math.ceil((project.numQuestion / totalQuestions) * 100)
                #print("Avanza a la pregunta: " + str(project.numQuestion))


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
        #print("Se produjo una excepción: "+str(e))
        return redirect('projects')

# Crea las politicas asociadas al proyecto
def createPolicies(project, user):
    policies = Policy.objects.all()
    policyDocuments = Text.objects.all()
    for policy in policies:
        
        #print("Creando las políticas del proyecto:", project.excludedPolicies, " - ", policy.orderPolicy)
        excludedPolicies = [int(value) for value in project.excludedPolicies]
        
        policyText = policyDocuments.get(orderText=policy.orderPolicy)

        # Si la política no está en la lista de excluidas el flag excluded es False, sino es True
        if policy.orderPolicy in excludedPolicies:
            ProjectPolicy.objects.create(project=project, policy=policy, orderProjectPolicy=policy.orderPolicy, excluded=True, content=policyText.content, fileName=policyText.fileName, createdBy=user, updatedBy=user)
        else:
            ProjectPolicy.objects.create(project=project, policy=policy, orderProjectPolicy=policy.orderPolicy, excluded=False, content=policyText.content, fileName=policyText.fileName, createdBy=user, updatedBy=user)


def createControls(project):
    controls = Control.objects.all()
    for control in controls:
        
        #print("Creando las politicas del proyecto:", project.excludedControls, " - ", control.orderControl)
        excludedControls = [int(value) for value in project.excludedControls]

        # Si la política no está en la lista de excluidas el flag excluded es False, sino es True
        if control.orderControl in excludedControls:
            ProjectControl.objects.create(project=project, control=control, orderProjectControl=control.orderControl, excluded=True)
        else:
            ProjectControl.objects.create(project=project, control=control, orderProjectControl=control.orderControl, excluded=False)


class ProjectListView(ListView):
    model = Project

class AnswerListView(ListView):
    model = Answer

class QuestionListView(ListView):
    model = Question


class TextUpdateView(UpdateView):
    model = Text
    form_class = TextForm
    template_name = 'core/textUpdate.html'

    def form_valid(self, form):
        messages.success(self.request, 'Documento actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar documento.')
        #print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse('textUpdate', args=[self.object.pk])


class TextProjectPolicyUpdateView(UpdateView):
    model = ProjectPolicy
    form_class = TextProjectPolicyForm
    template_name = 'core/textProjectPolicyUpdate.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is the owner of the project policy
        #print("Actualizar Documento")
        #print("self.object", self.get_object().createdBy)
        #print("request.user", request.user)
        projectPolicy = self.get_object()
        if request.user != projectPolicy.createdBy:
            raise Http404("Acceso denegado")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Documento actualizado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar documento.')
        #print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse('textProjectPolicyUpdate', args=[self.object.pk])


### GRÁFICAS
# Estadísticas de los proyectos
@login_required
def projectCharts(request):
    # Filter by Current User
    projectsUser = Project.objects.filter(createdBy=request.user)
    projects = list(projectsUser.values())
    context = {'projects': projects}
    return render(request, 'core/projectCharts.html', context)


@login_required
def policiesList(request, projectId):
    # Filter by Current User
    projectUser = Project.objects.get(id=projectId)
    draft = (ProjectPolicy.objects.filter(project=projectUser, createdBy=projectUser.createdBy, status="Borrador", excluded=False)).count()
    approved = (ProjectPolicy.objects.filter(project=projectUser, createdBy=projectUser.createdBy, status="Aprobado", excluded=False)).count()
    deprecated = (ProjectPolicy.objects.filter(project=projectUser, createdBy=projectUser.createdBy, status="Descontinuado",excluded=False)).count()
    
    data = {'policies': [
            ['Políticas', 'Estados'],
            ['Aprobado', approved],
            ['Descontinuado', deprecated],
            ['Borrador', draft],
        ]}
    return JsonResponse(data)

### AUTENTICACIÓN, REGISTRO, VALIDACIÓN DE USUARIOS

# Logout
def exit(request):
    logout(request)
    return redirect('home')


# User registration - queda deprecated - se usa ahora registerEmail
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


def registerEmail(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        #print("Entra a register_email")
        if form.is_valid():
            #print("Entra a register_email - is_valid")
            user = form.save()
            user.is_active = False  # Mark the user as inactive until they confirm their email
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Active su cuenta en M2J'
            if request.is_secure():
                protocol = "https"
            else:
                protocol = "http"

            message = render_to_string(
                'registration/activationEmail.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': protocol
                },
            )
            #print(message)
            email = EmailMessage(mail_subject, message, to=[user.email])
            email.content_subtype = 'html'
            emailsend = email.send()
            #print(emailsend)
            messages.info(request, 'Envió correo electrónico para activar su cuenta.')
            #Allow access to registration success page
            request.session['allowed_access'] = True
            return redirect('registrationSuccess')  # Create this view
        else:
            #print("Entra a register_email - is_invalid")
            data['form'] = form
            return render(request, 'registration/register.html', data)
            
    return render(request, 'registration/register.html', data)


def activate(request, uidb64, token):
    try:
        #print("Entra a activate")
        uid = force_str(urlsafe_base64_decode(uidb64))
        #print("uid", uid)
        user = User.objects.get(pk=uid)
        #print("user", user)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            #login(request, user)
            request.session['allowed_access'] = True
            return redirect('activationSuccess')
        else:
            return redirect('activationFailure')
    except Exception as e:
        #print("Se produjo una excepción: "+str(e))
        request.session['allowed_access'] = False
    return render(request, 'registration/activationInvalid.html')

def activationSuccess(request):
    return render(request, 'registration/activationSuccess.html')

def activationFailure(request):
    logout(request)
    return render(request, 'registration/activationFailure.html')

def registrationSuccess(request):
    return render(request, 'registration/registrationSuccess.html')

def activationInvalid(request):
    logout(request)
    return render(request, 'registration/activationInvalid.html')

def accessDenied(request):
    return render(request, 'registration/accessDenied.html')

#404 Not Found
def pageNotFound(request):
    return render(request, 'core/404.html', status=404)

# OTHERS
@login_required
def aboutUs(request):
    # projectsList = Project.objects.all()
    # projectsList = Project.objects.all().order_by('name')
    # return render(request, 'core/projects.html' , {'projects': projectsList})
    return render(request, 'core/aboutUs.html')