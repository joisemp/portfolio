from django.urls import path
from .import views

app_name = 'projects'

urlpatterns = [
    path('', views.WorkPageView.as_view(), name='work-page'),
    path('about/', views.AboutPageView.as_view(), name='about-page'),
    path('contact/', views.ContactPageView.as_view(), name='contact-page'),
]