from django.contrib import admin
from . import models

admin.site.register(models.ProgrammingProject)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('date', 'full_name', 'email_id')
    readonly_fields = ('date', 'full_name', 'email_id', 'subject', 'message')
