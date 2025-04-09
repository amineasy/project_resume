from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self, username, password, email=None, **extra_fields):
        if not username:
            raise ValueError('نام کاربری را وارد کنید')
        if not password:
            raise ValueError('رمز عبور را وارد کنید')
        if email:
            email = self.normalize_email(email)
            if self.model.objects.filter(email=email).exists():
                raise ValueError('ایمیل از قبل وجود دارد')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, username, password, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        self.create_user(username, password, email, **extra_fields)



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    email_confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
