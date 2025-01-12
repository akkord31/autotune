from django.urls import path
from . import views

urlpatterns = [
    path('', views.archive_view, name='archive'),
    path('add/', views.archive_add, name='archive_add'),
]
