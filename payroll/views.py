from django.shortcuts import render
from employees.models import Employee
from .forms import MonthSelectionForm

def payroll_view(request):
    form = MonthSelectionForm(request.GET or None)
    selected_month = None
    employees = []

    if form.is_valid():
        selected_month = form.cleaned_data['month']
        employees = Employee.objects.all()
        for employee in employees:
            employee.accrued = employee.salary  # Начислено
            employee.deducted = round(employee.salary * 0.118, 2)  # Удержано (11.8%)
            employee.to_pay = employee.accrued - employee.deducted  # К выдаче
            employee.child_sum = employee.children * 1400  # Сумма на детей
            employee.total_with_children = employee.to_pay + employee.child_sum  # Итоговая сумма

    return render(request, 'payroll/payroll.html', {
        'form': form,
        'employees': employees,
        'selected_month': selected_month,
    })
