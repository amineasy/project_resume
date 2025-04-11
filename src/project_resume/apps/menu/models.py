from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='sub_menu')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dishes")
    price = models.IntegerField()
    discount_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_total_price(self):
        if self.discount_price:
            discount_ratio = self.discount_price / 100
            return self.price-(self.price * discount_ratio)
        else:
            return self.price






