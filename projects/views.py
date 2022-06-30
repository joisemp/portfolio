from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . forms import ContactForm
from . emails import ContactEmail


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

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        sender_email_id = form.cleaned_data['email_id']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Send email
        ContactEmail(full_name, sender_email_id,
                     subject, message).send_to_admin()

        return super(ContactPageView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('projects:contact-page')


class ProgrammingProjectDetailView(generic.DetailView):
    model = models.ProgrammingProject
    template_name = 'projects/programming_project.html'
