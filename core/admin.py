from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'startDate', 'endDate', 'updated_at', 'created_at', 'createdBy', 'createdBy_id')
    list_filter = ('startDate', 'endDate', 'createdBy')
admin.site.register(Project, ProjectAdmin)

# Register your models here.
