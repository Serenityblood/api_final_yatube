from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        permission = False
        if obj.author == request.user:
            permission = True
        if request.method in permissions.SAFE_METHODS:
            permission = True
        return permission
