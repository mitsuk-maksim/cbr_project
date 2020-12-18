from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Проверяем, похож ли запрашивающий пользователь на пользовательское поле объекта
        Гарантирует, что владелец профиля - единственный, кто может изменить свою информацию.
        """
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
