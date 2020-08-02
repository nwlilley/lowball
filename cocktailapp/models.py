from django.db import models
from users.models import User


# Create your models here.
class Spirit(models.Model):
    name = models.CharField(max_length=100)
     = models.CharField(max_length=100)
    proof = models.CharField(max_length=100, blank=True)
    size = models.FloatField(default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brandname}'

    @property
    def price_per_oz(self):
        bottle_size_oz = float(self.size) * 33.814
        price_per_oz = round(float(self.price)/bottle_size_oz, 2)
        return price_per_oz