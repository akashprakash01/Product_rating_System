from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin()

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self,request, viiew, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and(request.user.is_admin() or obj.user == request.user)        