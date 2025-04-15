from django.db import models

from project_resume.apps.menu.models import User


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField()


    def __str__(self):
        return self.fullname




class Branch(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    working_days = models.CharField(max_length=120)

    def __str__(self):
        return self.name






