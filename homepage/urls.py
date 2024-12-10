from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('about-us/', views.about_us_view, name='about_us'),
]
