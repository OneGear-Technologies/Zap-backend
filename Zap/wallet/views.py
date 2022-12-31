from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import WalletSerializer
from .models import Wallet
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CreateWallet(APIView):
    serializer_class = WalletSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uid = get_object_or_404(User, username=request.user.username)
            wid = serializer.data.get('wid')
            amount = serializer.data.get('amount')
            queryset = Wallet.objects.filter(wid=wid)
            if queryset.exists():
                wallet = queryset[0]
                wallet.uid = uid
                wallet.wid = wid
                wallet.amount = amount
                wallet.save(update_fields = ['uid', 'wid','amount'])
                return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)

            else:
                wallet = Wallet(uid=uid, wid=wid, amount=amount)
                wallet.save()
                return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)