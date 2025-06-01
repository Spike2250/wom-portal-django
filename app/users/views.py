from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from .forms import UserCreateForm, UserUpdateForm, LoginForm
from ..utils import AuthorizationCheckMixin, UserPermissionsMixin


class UsersView(ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users/users.html'


class UserLoginView(SuccessMessageMixin,
                    LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_message = _('You are logged in')

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(SuccessMessageMixin,
                     LogoutView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')


class UserCreateView(SuccessMessageMixin,
                     CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')


class UserUpdateView(AuthorizationCheckMixin,
                     UserPermissionsMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')


class UserDeleteView(AuthorizationCheckMixin,
                     UserPermissionsMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
