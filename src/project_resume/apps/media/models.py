from django.db import models

from project_resume.apps.inbox.models import Branch


class DishImage(models.Model):
    image = models.ImageField(upload_to='dish_images/',blank=True,null=True)
    dish = models.ForeignKey('menu.Dish', on_delete=models.CASCADE,related_name='images',blank=True,null=True)













class BranchImage(models.Model):
    image = models.ImageField(upload_to='branch_images/',blank=True,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name='images',blank=True,null=True)








class MenuImage(models.Model):
    image = models.ImageField(upload_to='menu_images/',blank=True,null=True)
    menu = models.ForeignKey('menu.Menu', on_delete=models.CASCADE,related_name='images',blank=True,null=True)