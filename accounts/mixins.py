from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AdminAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts:login")
        return super().dispatch(request, *args, **kwargs)
    

class LoginRedirectMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("accounts:dashboard-project-list")
        return super().dispatch(request, *args, **kwargs)