from rest_framework.routers import DefaultRouter
from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonDeleteAPIView, LessonUpdateAPIView

app_name=MaterialsConfig.name
router = DefaultRouter()
router.register(r"Course", CourseViewSet, basename="course")





urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lesson/delete/<int:pk>/", LessonDeleteAPIView.as_view(), name="lesson_delete"),

] + router.urls