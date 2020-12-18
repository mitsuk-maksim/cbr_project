from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    # Получение всех профилей пользователей и создание новых профилей.
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # Извлекает данные профиля текущего авторизованного пользователя.
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile")
]