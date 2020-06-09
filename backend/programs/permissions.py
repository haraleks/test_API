from rest_framework import permissions


DENIED_PERMISSION_MESSAGE = 'Это действие вам не разрешено'


class SuperAdminAccessPermissions(permissions.BasePermission):
    message = DENIED_PERMISSION_MESSAGE

    def has_permission(self, request, view):
        return request.user.is_superuser


class AdminAccessPermission(permissions.BasePermission):
    message = DENIED_PERMISSION_MESSAGE

    def has_permission(self, request, view):
        return request.user.has_perm('api.admin')


class TeacherAccessPermissions(permissions.BasePermission):
    message = DENIED_PERMISSION_MESSAGE

    def has_permission(self, request, view):
        if request.user.has_perm('api.admin') or request.user.has_perm('api.teacher'):
            return True
        return False


class StudentAccessPermissions(permissions.BasePermission):
    message = DENIED_PERMISSION_MESSAGE

    def has_permission(self, request, view):
        if request.user.has_perm('api.admin') or request.user.has_perm('api.student'):
            return True
        return False
