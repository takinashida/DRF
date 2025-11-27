from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from materials.models import Course, Lesson
from django.contrib.auth.models import Group

User = get_user_model()


class CourseViewSetTests(APITestCase):
    def setUp(self):
        # создаём группу Managers
        self.moderator_group, _ = Group.objects.get_or_create(name="moderator")

        # обычный юзер
        self.user = User.objects.create_user(
            username="user", email="user@mail.com", password="pass123"
        )

        # менеджер
        self.manager = User.objects.create_user(
            username="manager", email="manager@mail.com", password="pass123"
        )
        self.manager.groups.add(self.moderator_group)

        self.course = Course.objects.create(
            name="Test",
            description="d",
            owner=self.user
        )

        self.url_list = reverse("materials:course-list")
        self.url_detail = lambda pk: reverse("materials:course-detail", args=[pk])

    # CREATE #####################################################
    def test_create_course_user_ok(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url_list, {"name": "New", "description": "D"})
        self.assertEqual(response.status_code, 201)

    def test_create_course_manager_forbidden(self):
        self.client.force_authenticate(self.manager)
        response = self.client.post(self.url_list, {"name": "New", "description": "D"})
        self.assertEqual(response.status_code, 403)

    # RETRIEVE ###################################################
    def test_retrieve_course_owner(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url_detail(self.course.id))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_course_manager_ok(self):
        self.client.force_authenticate(self.manager)
        response = self.client.get(self.url_detail(self.course.id))
        self.assertEqual(response.status_code, 200)

    # UPDATE #####################################################
    def test_update_course_owner(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url_detail(self.course.id), {"name": "Updated"})
        self.assertEqual(response.status_code, 200)

    def test_update_course_manager_ok(self):
        self.client.force_authenticate(self.manager)
        response = self.client.patch(self.url_detail(self.course.id), {"name": "Updated"})
        self.assertEqual(response.status_code, 200)

    # DELETE #####################################################
    def test_delete_course_owner(self):
        self.client.force_authenticate(self.user)
        response = self.client.delete(self.url_detail(self.course.id))
        self.assertEqual(response.status_code, 204)

    def test_delete_course_manager_forbidden(self):
        self.client.force_authenticate(self.manager)
        response = self.client.delete(self.url_detail(self.course.id))
        self.assertEqual(response.status_code, 403)

class LessonAPITests(APITestCase):
    def setUp(self):
        # Создаем группу Managers
        self.moderator_group, _ = Group.objects.get_or_create(name="moderator")

        # Обычный пользователь
        self.user = User.objects.create_user(
            username="user",
            email="user@mail.com",
            password="pass123"
        )

        # Менеджер
        self.manager = User.objects.create_user(
            username="manager",
            email="manager@mail.com",
            password="pass123"
        )
        self.manager.groups.add(self.moderator_group)

        # Создаем курс
        self.course = Course.objects.create(
            name="Course 1",
            description="D",
            owner=self.user
        )

        # Создаем урок
        self.lesson = Lesson.objects.create(
            name="Lesson 1",
            description="Desc",
            url="https://youtube.com/watch?v=123",
            course=self.course,
            owner=self.user
        )

        # URL’ы
        self.url_create = reverse("materials:lesson_create")
        self.url_list = reverse("materials:lesson_list")
        self.url_update = lambda pk: reverse("materials:lesson_update", args=[pk])
        self.url_detail = lambda pk: reverse("materials:lesson_retrieve", args=[pk])
        self.url_delete = lambda pk: reverse("materials:lesson_delete", args=[pk])

    # -----------------------------------------------------------
    # CREATE
    # -----------------------------------------------------------
    def test_create_lesson_user_allowed(self):
        self.client.force_authenticate(self.user)

        data = {
            "name": "New Lesson",
            "description": "New Desc",
            "url": "https://youtube.com/test",
            "course": self.course.id
        }

        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 201)

    def test_create_lesson_manager_forbidden(self):
        self.client.force_authenticate(self.manager)

        data = {
            "name": "New Lesson",
            "description": "New Desc",
            "url": "https://youtube.com/test",
            "course": self.course.id
        }

        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 403)

    # -----------------------------------------------------------
    # LIST
    # -----------------------------------------------------------
    def test_list_lessons_user_allowed(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)

    def test_list_lessons_manager_allowed(self):
        self.client.force_authenticate(self.manager)

        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)

    # -----------------------------------------------------------
    # RETRIEVE
    # -----------------------------------------------------------
    def test_retrieve_lesson_user_owner_allowed(self):
        self.client.force_authenticate(self.user)

        response = self.client.get(self.url_detail(self.lesson.id))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_lesson_manager_allowed(self):
        self.client.force_authenticate(self.manager)

        response = self.client.get(self.url_detail(self.lesson.id))
        self.assertEqual(response.status_code, 200)

    # -----------------------------------------------------------
    # UPDATE
    # -----------------------------------------------------------
    def test_update_lesson_user_owner_allowed(self):
        self.client.force_authenticate(self.user)

        response = self.client.patch(self.url_update(self.lesson.id), {"name": "Updated"})
        self.assertEqual(response.status_code, 200)

    def test_update_lesson_manager_allowed(self):
        self.client.force_authenticate(self.manager)

        response = self.client.patch(self.url_update(self.lesson.id), {"name": "Updated"})
        self.assertEqual(response.status_code, 200)

    # -----------------------------------------------------------
    # DELETE
    # -----------------------------------------------------------
    def test_delete_lesson_user_owner_allowed(self):
        self.client.force_authenticate(self.user)

        response = self.client.delete(self.url_delete(self.lesson.id))
        self.assertEqual(response.status_code, 204)

    def test_delete_lesson_manager_forbidden(self):
        self.client.force_authenticate(self.manager)

        response = self.client.delete(self.url_delete(self.lesson.id))
        self.assertEqual(response.status_code, 403)