from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from materials.serializers import CourseSerializer, LessonSerializer
from users.models import User
from materials.models import Payment

class  UserSerializer(serializers.ModelSerializer):
    # payments=serializers.SerializerMethodField()

    class Meta:
        model= User
        fields = ["username","email", "password", "avatar", "phone_number", "city"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        hash_password = make_password(password)
        validated_data["password"] = hash_password
        instance = User(**validated_data)
        instance.save()
        return instance

    # def get_payments(self, obj):
    #     return PaymentSerializer(obj.payment.filter, many=True ).data

class  PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    buyed_course = CourseSerializer(many=False)
    buyed_lesson = LessonSerializer(many=False)

    class Meta:
        model= Payment
        fields = ["id","date","payment","type_payment","user","buyed_course","buyed_lesson"]
        depth = 1


