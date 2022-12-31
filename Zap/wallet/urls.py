from django.urls import path,include
from .views import CreateWallet

urlpatterns = [
    path('', CreateWallet.as_view())
]
