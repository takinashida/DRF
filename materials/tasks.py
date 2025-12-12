from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from materials.models import Course, Subscription

User = get_user_model()

@shared_task
def send_course_update_notifications(course_id):
    course = Course.objects.get(id=course_id)
    subs = Subscription.objects.filter(subed_course=course)

    emails = [sub.user.email for sub in subs if sub.user.email]

    if not emails:
        return "Нет подписчиков"

    send_mail(
        subject=f"Обновление курса: {course.name}",
        message="Курс был обновлен",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
    )

    return f"Отправлено писем: {len(emails)}"

@shared_task
def check_inactive_users():
    threshold = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=threshold)

    for user in inactive_users:
        print(f"Пользователь {user.username} не заходил 30 дней")
        user.is_active = False

    return f"Найдено пользователей: {inactive_users.count()}"
