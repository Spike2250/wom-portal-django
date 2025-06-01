from django.utils.translation import gettext as _
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class AuthorizationCheckMixin(LoginRequiredMixin):
    """
    Checks permissions to the pages.
    If user isn't logged in, redirects to the login page.
    """

    login_url = reverse_lazy('login')
    permission_denied_message = _('You are not logged in! Please log in.')
    redirect_field_name = None

    def get_login_url(self):
        messages.error(self.request, self.permission_denied_message)
        return str(self.login_url)


class UserPermissionsMixin(UserPassesTestMixin):
    """
    Checks updating / deleting (user profile) permissions.
    If the selected user is not the current user,
    user will not be updating / deleting.
    """

    def test_func(self):
        current_user = self.request.user.id
        chosen_user = self.kwargs['pk']

        if current_user != chosen_user:
            return False
        return True

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request,
                           _('You have no rights to change another user.'))
            return redirect(reverse_lazy('users'))
        return super().handle_no_permission()
