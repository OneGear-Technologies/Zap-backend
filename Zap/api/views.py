from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer,CreateWalletSerializer
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .models import Wallet
from django.http import HttpResponseRedirect

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



class CreateWallet(APIView):
    serializer_class = CreateWalletSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            wid = serializer.data.get('wid')
            _uid = serializer.data.get('uid')
            uid = User.objects.get(username=_uid)
            amount = serializer.data.get('amount')
            queryset = Wallet.objects.filter(wid = wid)
            if queryset.exists():
                wallet = queryset[0]
                wallet.uid = uid
                wallet.amount = amount
                wallet.save(update_fields=['uid', 'amount'])
                self.request.session['wid'] = wallet.wid
                return HttpResponseRedirect('api/', status=status.HTTP_200_OK)

            else:
                wallet = Wallet(uid=uid, wid=wid, amount=amount)
                self.request.session['uid'] = uid
                wallet.save()

                return HttpResponseRedirect('api/', status=status.HTTP_200_OK)
            