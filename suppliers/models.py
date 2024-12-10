# suppliers/models.py
from django.db import models

class Supplier(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name}"
