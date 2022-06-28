from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . forms import ContactForm


class WorkPageView(generic.TemplateView):
    template_name = 'projects/work.html'

    def get_context_data(self, **kwargs):
        context = super(WorkPageView, self).get_context_data(**kwargs)
        context['programming_projects'] = models.ProgrammingProject.objects.all(
        ).order_by('-year')
        return context


class AboutPageView(generic.TemplateView):
    template_name = 'projects/about.html'


class ContactPageView(generic.CreateView):
    model = models.Contact
    template_name = 'projects/contact.html'
    form_class = ContactForm
    
    def get_success_url(self):
        return reverse_lazy('projects:contact-page')
