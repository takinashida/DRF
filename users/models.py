from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, verbose_name="Имя пользователя")
    email = models.CharField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True)
    city = models.CharField(verbose_name="Город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username