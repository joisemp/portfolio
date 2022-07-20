
from django.urls import path
from .import views

app_name = 'projects'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('about/', views.AboutPageView.as_view(), name='about-page'),
    path('contact/', views.ContactPageView.as_view(), name='contact-page'),
    path('projects/', views.ProjectListPageView.as_view(),
         name='project-list-page'),
    path('projects/filter=programming-projects/',
         views.ProgrammingProjectFilterView.as_view(), name='programming-project-filter-page'),
    path('projects/filter=design-projects/',
         views.DesignProjectFilterView.as_view(), name='design-project-filter-page'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(),
         name='project-detail-page'),
]
