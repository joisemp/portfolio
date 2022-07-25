from django.urls import reverse_lazy
from . forms import CustomAuthenticationForm
from django.contrib.auth import views
from django.contrib.auth import login
from django.contrib import messages


class LoginView(views.LoginView):
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
        return reverse_lazy('projects:home-page')


class UserLogoutView(views.LogoutView):
    template_name = 'accounts/logged_out.html'


class ChangePasswordView(views.PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('projects:home-page')


class ResetPasswordView(views.PasswordResetView):
    email_template_name = 'accounts/password_reset/password_reset_email.html'
    html_email_template_name = 'accounts/password_reset/password_reset_email.html'
    subject_template_name = 'accounts/password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:done-password-reset')
    template_name = 'accounts/password_reset/password_reset_form.html'


class DonePasswordResetView(views.PasswordResetDoneView):
    template_name = 'accounts/password_reset/password_reset_done.html'


class ConfirmPasswordResetView(views.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:complete-password-reset')
    template_name = 'accounts/password_reset/password_reset_confirm.html'


class CompletePasswordResetView(views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset/password_reset_complete.html'
