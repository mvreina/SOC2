from django.contrib import admin
from .models import Project, Question, Answer, ProjectQuestion, Policy, ProjectPolicy, Text, Control, ProjectControl

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
    list_filter = ('project', 'question', 'answer', 'orderProjectQuestion')

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('orderPolicy', 'name', 'category')
    list_filter = ('category', 'orderPolicy')
    sortable_by = ('orderPolicy')

class ProjectPolicyAdmin(admin.ModelAdmin):
    list_display = ('project', 'policy', 'excluded', 'orderProjectPolicy')
    list_filter = ('project', 'policy', 'excluded')
    sortable_by = ('orderProjectPolicy')


class TextAdmin(admin.ModelAdmin):
    list_display = ('orderText', 'name', 'fileName')
    list_filter = ('name', 'orderText')


class ControlAdmin(admin.ModelAdmin):
    list_display = ('orderControl', 'name', 'policy')
    list_filter = ('name', 'orderControl')
    sortable_by = ('orderControl', 'name')

class ProjectControlAdmin(admin.ModelAdmin):
    list_display = ('project', 'control', 'excluded', 'orderProjectControl')
    list_filter = ('project', 'control', 'excluded')
    sortable_by = ('orderProjectControl')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ProjectQuestion, ProjectQuestionAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(ProjectPolicy, ProjectPolicyAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Control, ControlAdmin)
admin.site.register(ProjectControl, ProjectControlAdmin)