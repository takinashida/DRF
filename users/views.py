from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from users.models import User
from users.serializers import UserSerializer, PaymentSerializer
from materials.models import Payment
from users.services.stripe_service import create_product, create_price, create_checkout_session, retrieve_session


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

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        product = create_product(payment.buyed_course.name)
        price = create_price(product.id, payment.payment)
        session = create_checkout_session(
            price_id=price.id,
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cancel/"
        )

        payment.stripe_session_id = session.id
        payment.payment_url = session.url
        payment.save()


class PaymentStatusAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        payment = self.get_object()
        session = retrieve_session(payment.stripe_session_id)
        return Response({"status": session.status})

