from django.urls import path
from .views import RegisterView, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views
from api import views as user_views

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='api/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
]