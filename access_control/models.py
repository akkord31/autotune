from django.db import models
from django.contrib.auth.models import User


class AccessControl(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    view_homepage = models.IntegerField()
    view_about = models.IntegerField()
    view_services = models.IntegerField()
    view_suppliers = models.IntegerField()
    view_employees = models.IntegerField()
    view_salary = models.IntegerField()
    view_reports = models.IntegerField()
    view_access_system = models.IntegerField()
    view_archive = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - Access Control"
