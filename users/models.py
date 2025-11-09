from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


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



class Payment(models.Model):
    PAYMENT_CHOICES = (
        ("card", "Оплата картой"),
        ("cash", "Оплата наличными"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment', verbose_name="Пользователь")
    date = models.DateField(verbose_name="Дата платежа")
    buyed_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment', verbose_name="Курс",  blank=True, null=True)
    buyed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payment', verbose_name="Урок",  blank=True, null=True)
    payment = models.IntegerField(verbose_name="Сумма платежа")
    type_payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, verbose_name="Тип оплаты")


    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):
        return self.date