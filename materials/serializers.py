from rest_framework import serializers

from materials.models import Lesson, Course



class  CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField()

    class Meta:
        model= Course
        fields = ["name", "description", "lessons_count", "lessons_info", "preview", "owner"]

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_lessons_info(self, obj):
        lessons = obj.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return serializer.data




class  LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model= Lesson
        fields = "__all__"


