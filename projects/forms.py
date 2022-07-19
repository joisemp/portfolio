from django import forms
from .models import Contact, Project

PROJECT_TYPE = (
    ("Programming", "Programming"),
    ("Design", "Design"),
)

ROLE = (
    ("Full Stack Developer", "Full Stack Developer"),
    ("Web-Designer", "Web-Designer"),
    ("Designer", "Designer"),
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email_id', 'subject', 'message')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'project_type': forms.Select(choices=PROJECT_TYPE),
            'role': forms.Select(choices=ROLE),
        }
