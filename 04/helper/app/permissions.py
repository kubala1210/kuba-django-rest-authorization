from rest_framework import permissions
from .acl import acl_check


class ACLPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        mapping = {
            'GET': 'read',
            'PUT': 'update',
            'PATCH': 'update',
            'DELETE': 'delete'
        }

        action = mapping.get(request.method, 'read')

        return acl_check(request.user, obj, action)
