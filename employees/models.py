from django.db import models


class Employee(models.Model):
    tab_number = models.IntegerField(unique=True)
    surname = models.CharField(max_length=50)
    salary = models.FloatField(max_length=50)
    children = models.IntegerField()

    def __str__(self):
        return f"{self.surname} - {self.salary}₽"
