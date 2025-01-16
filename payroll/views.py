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
            employee.accrued = employee.salary

            if employee.children < 3:
                employee.child_sum = employee.children * 1400
            else:
                employee.child_sum = 2800 + (employee.children - 2) * 3000

            if employee.accrued - employee.child_sum < 280000:
                employee.deducted = round((employee.accrued - employee.child_sum) * 0.13, 2)
            else:
                employee.deducted = round(employee.accrued * 0.13, 2)

            employee.to_pay = employee.accrued - employee.deducted

            employee.total_with_children = employee.to_pay + employee.child_sum

    return render(request, 'payroll/payroll.html', {
        'form': form,
        'employees': employees,
        'selected_month': selected_month,
    })