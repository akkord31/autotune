from django.db import models
from services.models import Service, Car


class ServiceArchive(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_date = models.DateField()
    final_price = models.FloatField()

    def __str__(self):
        return f"{self.car} - {self.service.name} - {self.service_date} - {self.final_price} рублей"
