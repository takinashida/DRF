from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["buyed_course", "buyed_lesson", "type_payment"]
    ordering_fields = ["date"]