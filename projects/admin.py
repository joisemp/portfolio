from django.contrib import admin
from . import models
from . forms import ProjectForm


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_type', 'title')
    form = ProjectForm


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('date', 'full_name', 'email_id')
    readonly_fields = ('date', 'full_name', 'email_id', 'subject', 'message')
