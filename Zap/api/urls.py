from django.urls import path
from .views import RegisterView, AllView

urlpatterns = [
    path('', AllView.as_view()),
    path('register/', RegisterView.as_view())
]