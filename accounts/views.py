from django.urls import reverse_lazy
from . forms import CustomAuthenticationForm
from django.contrib.auth import views
from django.contrib.auth import login
from django.contrib import messages
from django.views import generic
from projects import models
from .mixins import AdminAccessMixin, LoginRedirectMixin
from projects.forms import ProjectForm


class LoginView(LoginRedirectMixin, views.LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)

        message = "You have logged in successfully"
        messages.success(self.request, message)

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:dashboard-project-list')


class UserLogoutView(views.LogoutView):
    template_name = 'accounts/logged_out.html'


class ChangePasswordView(AdminAccessMixin, views.PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('accounts:dashboard-project-list')


class ResetPasswordView(LoginRedirectMixin, views.PasswordResetView):
    email_template_name = 'accounts/password_reset/password_reset_email.html'
    html_email_template_name = 'accounts/password_reset/password_reset_email.html'
    subject_template_name = 'accounts/password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:done-password-reset')
    template_name = 'accounts/password_reset/password_reset_form.html'


class DonePasswordResetView(LoginRedirectMixin, views.PasswordResetDoneView):
    template_name = 'accounts/password_reset/password_reset_done.html'


class ConfirmPasswordResetView(LoginRedirectMixin, views.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:complete-password-reset')
    template_name = 'accounts/password_reset/password_reset_confirm.html'


class CompletePasswordResetView(LoginRedirectMixin, views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset/password_reset_complete.html'


class DashboardProjectListView(AdminAccessMixin, generic.ListView):
    template_name = 'accounts/dashboard-project-list.html'
    model = models.Project
    context_object_name = 'projects'
    queryset = models.Project.objects.order_by('-id')


class ProjectUpdateView(AdminAccessMixin, generic.UpdateView):
    model = models.Project
    form_class = ProjectForm
    template_name = 'accounts/project_update.html'
    success_url = reverse_lazy('accounts:dashboard-project-list')

    def form_valid(self, form):
        message = "Model Updated Successfully"
        messages.success(self.request, message)
        return super(ProjectUpdateView, self).form_valid(form)


class ProjectCreateView(AdminAccessMixin, generic.CreateView):
    model = models.Project
    form_class = ProjectForm
    template_name = 'accounts/project_create.html'
    success_url = reverse_lazy('accounts:dashboard-project-list')

    def form_valid(self, form):
        message = "Project created Successfully"
        messages.success(self.request, message)
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDeleteView(AdminAccessMixin, generic.DeleteView):
    model = models.Project
    template_name = 'accounts/project_delete.html'
    success_url = reverse_lazy('accounts:dashboard-project-list')

    def delete(self, request, *args, **kwargs):
        message = "Project deleted Successfully"
        messages.success(self.request, message)
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)


class ContactListView(AdminAccessMixin, generic.ListView):
    template_name = 'accounts/dashboard-contact-list.html'
    model = models.Contact
    context_object_name = 'contacts'
    queryset = models.Contact.objects.order_by('-id')


class ProjectSerchView(generic.ListView):
    model = models.Project
    template_name = 'accounts/dashboard-project-list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        query = self.request.GET.get('search_item')
        return models.Project.objects.filter(title__icontains=query).order_by('-id')
