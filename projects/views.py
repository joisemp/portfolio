from django.shortcuts import render
from django.views import generic
from . import models

class WorkPageView(generic.TemplateView):
    template_name = 'projects/work.html'
    
    def get_context_data(self, **kwargs):
        context = super(WorkPageView, self).get_context_data(**kwargs)
        context['programming_projects'] = models.ProgrammingProject.objects.all().order_by('-year')
        return context
    
class AboutPageView(generic.TemplateView):
    template_name = 'projects/about.html'