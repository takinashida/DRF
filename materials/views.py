from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics , permissions

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = (~IsModerator)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerator | IsOwner)
        if self.action in ["destroy"]:
            self.permission_classes = (~IsModerator,IsOwner)
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

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
    permission_classes = [permissions.IsAuthenticated, ~IsModerator, IsOwner]
