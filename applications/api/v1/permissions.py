from rest_framework import permissions


class IsAppOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an app to edit it.
    Read-only access is allowed for everyone.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow authenticated users who are developers to create/modify apps
        return request.user.is_authenticated and request.user.is_developer

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow the app owner to modify the app
        return obj.owner == request.user
