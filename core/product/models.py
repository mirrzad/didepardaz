from django.db import models
from django.core.validators import MinValueValidator


class Brand(models.Model):
    """
    Stores a single brand entry.
    """
    title = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Stores a single product entry related to model:product.Brand.
    """
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=200)
    screen_size = models.FloatField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    made_in = models.CharField(max_length=200)

    def __str__(self):
        return self.title
