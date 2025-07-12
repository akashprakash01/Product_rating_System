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


class IsAdminForUpdateDelete(permissions.BasePermission):
    """
    Allow PUT, PATCH, DELETE only for admins.
    Allow GET, HEAD, OPTIONS for all authenticated users.
    """
    def has_permission(self, request, view):
        # Safe methods like GET, HEAD, OPTIONS → allowed for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # PUT, PATCH, DELETE → only allowed for admins
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and request.user.is_admin()

        # POST or others → allow for authenticated users
        return request.user.is_authenticated
