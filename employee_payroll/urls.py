from django.urls import path
from .views import payroll_view  # Импорт представления для отображения списка выплат

urlpatterns = [
    path('', payroll_view, name='payroll_list'),
]