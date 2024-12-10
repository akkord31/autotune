from django.shortcuts import render

from access_control.decorators import permission_required
from .models import Employee  # Импорт модели Employee


@permission_required('employees')
def employee_list(request):
    employees = Employee.objects.all()  # Получение всех сотрудников из базы данных
    return render(request, 'employees/employees.html', {'employees': employees})
