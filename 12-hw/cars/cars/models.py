from django.db import models

class CarType(models.TextChoices):
    TOYOTA = "Toyota", "Toyota"
    HONDA = "Honda", "Honda"
    RENAULT = "Renault", "Renault"
    UNKNOWN = "Unknown", "Unknown"

class Cars(models.Model):
    car_type = models.CharField(
        max_length=20,
        choices=CarType.choices,
        default=CarType.UNKNOWN
    )
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.car_type} {self.model} ({self.year})"
