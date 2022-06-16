from django.urls import path
from .import views

app_name = 'projects'

urlpatterns = [
    path('', views.WorkPageView.as_view(), name='work-page')
]