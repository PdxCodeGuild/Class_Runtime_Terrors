from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny


class IsSysAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_sysadmin


class IsMerchant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_merchant