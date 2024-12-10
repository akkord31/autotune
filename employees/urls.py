from django.urls import path

from employees import views as employees_views
from homepage import views as homepage_views

urlpatterns = [
    path('', employees_views.employee_list, name='employees'),
]
