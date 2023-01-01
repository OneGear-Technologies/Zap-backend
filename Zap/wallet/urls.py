from django.urls import path
from .views import CreateWallet,WalletView,UpdateWallet
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', WalletView.as_view()),
    path('create/', login_required(CreateWallet.as_view())),
    path('update/', login_required(UpdateWallet.as_view()))
]
