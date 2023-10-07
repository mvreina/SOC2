from django.contrib import admin
from .models import Project, Question, Answer, ProjectQuestion

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'numQuestion','createdBy_id', 'id')
    list_filter = ('name', 'numQuestion')


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'updated_at', 'created_at', 'createdBy', 'updatedBy')
    list_filter = ('name', 'createdBy')
    inlines = [
        AnswerInline
    ]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'type', 'orderAnswer', 'updated_at', 'created_at', 'createdBy', 'updatedBy')
    list_filter = ('createdBy', 'question')


class QuestionInline(admin.TabularInline):
    model = Question

class ProjectInline(admin.TabularInline):
    model = Project


class ProjectQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'userAnswer', 'orderProjectQuestion')
    list_filter = ('orderProjectQuestion', 'question', 'answer')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ProjectQuestion, ProjectQuestionAdmin)