from rest_framework.permissions import BasePermission


class IsPermitted(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        return False