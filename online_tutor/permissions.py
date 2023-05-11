from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsSuper(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_superuser)


class IsPermitted(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff and request.user == obj.user)


