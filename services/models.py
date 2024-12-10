from django.db import models


class Service(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    supplier_code = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.price} рублей"


class Car(models.Model):
    code = models.IntegerField(unique=True)
    brand = models.CharField(max_length=50)
    coefficient = models.FloatField()

    def __str__(self):
        return f"{self.brand} - {self.coefficient}%"
