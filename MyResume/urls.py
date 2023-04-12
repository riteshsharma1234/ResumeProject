from django.urls import path

from . import views

urlpatterns =[
    path('', views.aboutme_view, name='aboutme'),
    path('skills/',views.skills_view,name='skills'),
    path('qualification/',views.qualification,name='qualification'),
    path('projects/',views.projects_view,name='projects'),
    path('Experience/',views.Experience_view,name='Experience'),
    path('contact/',views.contact,name='contact')
]