from socket import getnameinfo
from django.shortcuts import render
from django.views import generic

class WorkPageView(generic.TemplateView):
    template_name = 'projects/work.html'