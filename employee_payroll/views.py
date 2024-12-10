from django.shortcuts import render
from .models import EmployeePayroll


def payroll_view(request):
    payrolls = EmployeePayroll.objects.select_related('employee').all()

    for payroll in payrolls:
        payroll.to_issue_value = payroll.to_issue()
        payroll.for_children_value = payroll.for_children()

    return render(request, 'payroll.html', {'payrolls': payrolls})
