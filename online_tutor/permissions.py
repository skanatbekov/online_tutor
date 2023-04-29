from rest_framework.permissions import BasePermission


class IsSuper(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True
        return False


class IsPermittedObj(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        return False


class IsPermitted(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        return False
