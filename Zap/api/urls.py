from django.urls import path
from .views import RegisterView, MyObtainTokenPairView, CreateWallet
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('wallet/', CreateWallet.as_view())
]