from django.db import models

from users.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='course_preview/',  null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course', verbose_name="Создатель", blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='lesson_preview/', null=True, blank=True)
    url = models.URLField(verbose_name="Ссылка")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name="Курс")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons', verbose_name="Создатель", blank=True, null=True)

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name


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
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    payment_url = models.URLField(blank=True, null=True)


    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):
        return self.date

class Subscription(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription', verbose_name="Пользователь")
    subed_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscription', verbose_name="Курс")



    class Meta:
        unique_together = ("user", "subed_course")
        verbose_name = "подписка"
        verbose_name_plural = "подписка"

    def __str__(self):
        return self.user.username




