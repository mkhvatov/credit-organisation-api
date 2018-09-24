from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class SuperUserPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser:
                return True

        raise PermissionDenied


class PartnerPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner:
                return True

        raise PermissionDenied


class PartnerAndSuperUserPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner or request.user.is_superuser:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner or request.user.is_superuser:
                return True

        raise PermissionDenied


class CreditOrganizationPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.profile.is_credit_organization:
            return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user.profile.is_credit_organization:
            return True

        raise PermissionDenied


class PartnerCreditOrganizationSuperUserPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner or request.user.profile.is_credit_organization \
                    or request.user.is_superuser:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_partner or request.user.profile.is_credit_organization \
                    or request.user.is_superuser:
                return True

        raise PermissionDenied


class CreditOrganizationAndSuperUserPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_credit_organization or request.user.is_superuser:
                return True

        raise PermissionDenied

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.profile.is_credit_organization or request.user.is_superuser:
                return True

        raise PermissionDenied
