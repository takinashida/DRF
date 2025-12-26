from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics , permissions
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import StandardPagination
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner
from materials.tasks import send_course_update_notifications


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardPagination

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [~IsModerator]
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = [IsModerator | IsOwner]
        if self.action in ["destroy"]:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        old_updated = self.get_object().updated
        course = serializer.save()

        if timezone.now() - old_updated >= timedelta(hours=4):
            send_course_update_notifications.delay(course.id)

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsModerator | IsOwner]
    pagination_class = StandardPagination

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsModerator | IsOwner]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsModerator | IsOwner]

class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]




class SubscriptionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get("course_id")
        course = Course.objects.get(id=course_id)

        sub_qs = Subscription.objects.filter(user=user, course=course)

        if sub_qs.exists():
            sub_qs.delete()
            message = "подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course)
            message = "подписка добавлена"

        return Response({"message": message})



