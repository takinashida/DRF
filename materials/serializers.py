from rest_framework import serializers

from materials.models import Lesson, Course, Subscription
from materials.validators import validate_url


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
    url = serializers.CharField(validators=[validate_url])

    class Meta:
        model= Lesson
        fields = "__all__"


class  SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model= Subscription
        fields = "__all__"

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        return obj.subscriptions.filter(user=user).exists()


