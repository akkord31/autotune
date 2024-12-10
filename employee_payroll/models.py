from django.db import models
from employees.models import Employee  # Импорт модели Employee из другого приложения


class EmployeePayroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payrolls')
    withheld = models.DecimalField("Удержанно", max_digits=10, decimal_places=2)
    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)

    def to_issue(self):
        """Вычисляемое поле: К выдаче"""
        return self.employee.salary - self.withheld

    def for_children(self):
        """Вычисляемое поле: На детей"""
        return self.employee.children * 1400 if self.employee.children > 0 else 0
