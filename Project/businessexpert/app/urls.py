
from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='index'),
    path('home/', views.home_view, name='index'),
    path('services/', views.services_view, name='services'),
    path('process/', views.process_view, name='process'),
    path('blog/', views.blog_view, name='blog'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

]
