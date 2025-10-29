from django.db import models



# Create your models here.

class Lesson(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='lesson_preview/', null=True, blank=True)
    url = models.URLField(verbose_name="Ссылка")


    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to='course_preview/',  null=True, blank=True)
    lessons =models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name

