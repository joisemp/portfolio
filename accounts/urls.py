from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('change-password/', views.ChangePasswordView.as_view(),
         name='change-password'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
    path('done-password-reset/', views.DonePasswordResetView.as_view(),
         name='done-password-reset'),
    path('confirm-password-reset/<uidb64>/<token>/',
         views.ConfirmPasswordResetView.as_view(), name='confirm-password-reset'),
    path('complete-password-reset/', views.CompletePasswordResetView.as_view(),
         name='complete-password-reset'),
    path('dashboard/', views.DashboardProjectListView.as_view(), name='dashboard-project-list'),
]
