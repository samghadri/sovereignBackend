from rest_framework.permissions import BasePermission

from django.contrib.auth import get_user_model

User = get_user_model()


class IsAuthenticated(BasePermission):
    """
    Custom version of IsAuthenticated permission.

    We need to ensure that the authenticated user is an API user,
    otherwise a logged-in CMS user will be seen as authenticated,
    but will fail to access anything as they won't have a QSS ID
    or package code.
    """

    def has_permission(self, request, view):
        return isinstance(request.user, User) and request.user.is_authenticated


class RequiresAuthenticationMixin(object):
    """
    Adds our custom authentication via ABS to a view
    """
    permission_classes = (IsAuthenticated,)
