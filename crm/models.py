from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=50)
    city_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.street} {self.street_number}, {self.city}"

