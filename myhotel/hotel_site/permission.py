from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'