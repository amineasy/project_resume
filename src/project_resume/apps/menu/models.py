from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models






class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='sub_menu_related')

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dishes")
    price = models.IntegerField()
    discount_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)



    def __str__(self):
        return self.name

    def get_total_price(self):
        if self.discount_price:
            discount_ratio = self.discount_price / 100
            return self.price-(self.price * discount_ratio)
        else:
            return self.price




class RatingDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings")
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])


    class Meta:
        unique_together = (('dish', 'user'),)



    def __str__(self):
        return f"{self.user} rated {self.dish.name} with score {self.score}"





class LikeDish(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = (('user', 'dish'),)

    def __str__(self):
        return f"{self.user} liked {self.dish.name}"