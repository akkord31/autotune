from django.shortcuts import render
from employees.models import Employee
from .forms import MonthSelectionForm
import calendar


MONTH_TRANSLATIONS = {
    'January': 'Январь',
    'February': 'Февраль',
    'March': 'Март',
    'April': 'Апрель',
    'May': 'Май',
    'June': 'Июнь',
    'July': 'Июль',
    'August': 'Август',
    'September': 'Сентябрь',
    'October': 'Октябрь',
    'November': 'Ноябрь',
    'December': 'Декабрь',
}


def payroll_view(request):
    form = MonthSelectionForm(request.GET or None)
    selected_month = None
    employees = []

    if form.is_valid():
        month_number = form.cleaned_data['month']
        selected_month = MONTH_TRANSLATIONS[calendar.month_name[int(month_number)]]
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
