

from django.urls import path
from .views import NavItemsAPIView, RegisterView, LoginView, UserView

urlpatterns = [
    path('nav/', NavItemsAPIView.as_view()),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/user/', UserView.as_view()),
]
