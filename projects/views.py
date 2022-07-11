from django.shortcuts import render
from django.views import generic
from . import models
from . forms import ContactForm
from . mail import ContactEmail
from django.urls import reverse_lazy


class HomePageView(generic.ListView):
    template_name = 'projects/home.html'
    model = models.Project


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


class ProjectDetailView(generic.DetailView):
    model = models.Project
    template_name = 'projects/project_detail.html'