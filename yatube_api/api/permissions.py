from rest_framework import permissions


class AuthorOrAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_authenticated
           or request.method in permissions.SAFE_METHODS):
            return True
        elif (not request.user.is_authenticated
              and request.method not in permissions.SAFE_METHODS):
            return False

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
