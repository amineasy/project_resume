from django.db import models


class DishImage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    dish = models.ForeignKey('menu.Dish', on_delete=models.CASCADE)
