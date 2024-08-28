from django.urls import path
from .views import UserDetailView, UserCreateView

urlpatterns = [
    path('users/me/', UserDetailView.as_view()),
    path('users/signup/', UserCreateView.as_view()),
]