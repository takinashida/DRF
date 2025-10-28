from django.db import models



# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='course_preview/')

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='lesson_preview/')
    url = models.URLField(verbose_name="Название")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name