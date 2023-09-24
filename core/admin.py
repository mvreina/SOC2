from django.contrib import admin
from .models import Project, Question, Answer

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'startDate', 'endDate', 'updated_at', 'created_at', 'createdBy', 'createdBy_id')
    list_filter = ('startDate', 'endDate', 'createdBy')


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'order', 'updated_at', 'created_at', 'createdBy', 'updatedBy')
    list_filter = ('order', 'createdBy')
    ordering = ('order', 'createdBy')
    inlines = [
        AnswerInline
    ]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'type', 'text', 'order', 'updated_at', 'created_at', 'createdBy', 'updatedBy')
    list_filter = ('order', 'createdBy', 'question')
    ordering = ('question', 'order')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

