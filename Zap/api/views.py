from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, CreateUserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone = serializer.data.get('phone')
            charge_stat = serializer.data.get('charge_stat')
            host = self.request.session.session_key
            queryset = User.objects.filter(host = host)
            if queryset.exists():
                user = queryset[0]
                user.phone = phone
                user.charge_stat = charge_stat
                user.save(update_fields = ['charge_stat', 'phone'])
                self.request.session['code'] = user.code
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

            else:
                user = User(host=host, charge_stat=charge_stat, phone=phone)
                self.request.session['code'] = user.code
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)