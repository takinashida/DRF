from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics , permissions

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
