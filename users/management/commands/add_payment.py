from datetime import date

from django.core.management import BaseCommand
from materials.models import Course, Lesson
from users.models import User
from materials.models import Payment

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
            user1, user_created = User.objects.get_or_create(username="freder", email="freder@example.com", city="Москва")
            user1.set_password("qwerty123")
            user1.save()

            course1, course_created = Course.objects.get_or_create(name="Django для начинающих", description="Основы веб-разработки на Django")
            course1.save()

            lesson1, lesson_created = Lesson.objects.get_or_create(name="Введение в Django", course=course1)
            lesson1.save()

            payment1, payment_created = Payment.objects.get_or_create(
                user=user1,
                date=date.today(),
                buyed_course=course1,
                payment=2990,
                type_payment="card"
            )
            payment1.save()