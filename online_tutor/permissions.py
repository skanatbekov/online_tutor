from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsSuperObj(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)


class IsSuper(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsPermittedObj(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)


class IsPermitted(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

