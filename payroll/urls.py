from django.urls import path
from .views import payroll_view

urlpatterns = [
    path('', payroll_view, name='payroll_list'),
]
