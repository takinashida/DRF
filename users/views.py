from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from users.models import User
from users.serializers import UserSerializer, PaymentSerializer
from materials.models import Payment

# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["buyed_course", "buyed_lesson", "type_payment"]
    ordering_fields = ["date"]
    permission_classes = [permissions.IsAuthenticated]