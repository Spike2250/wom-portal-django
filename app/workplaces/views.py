from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from .forms import WorkplaceForm
from .models import Workplace
from ..utils import AuthorizationCheckMixin


class WorkplaceView(AuthorizationCheckMixin,
                    DetailView):
    model = Workplace
    template_name = 'workplaces/workplace.html'


class WorkplacesView(AuthorizationCheckMixin,
                     ListView):
    model = Workplace
    context_object_name = 'workplaces'
    template_name = 'workplaces/workplaces.html'


class WorkplaceCreateView(AuthorizationCheckMixin,
                          SuccessMessageMixin,
                          CreateView):
    form_class = WorkplaceForm
    template_name = 'workplaces/create.html'
    success_url = reverse_lazy('workplaces')
    success_message = _('Workplace successfully created')

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.creator = current_user
        return super().form_valid(form)


class WorkplaceUpdateView(AuthorizationCheckMixin,
                          SuccessMessageMixin,
                          UpdateView):
    model = Workplace
    form_class = WorkplaceForm
    template_name = 'workplaces/update.html'
    success_url = reverse_lazy('workplaces')
    success_message = _('Workplace successfully updated')


class WorkplaceDeleteView(AuthorizationCheckMixin,
                          SuccessMessageMixin,
                          DeleteView):
    model = Workplace
    template_name = 'workplaces/delete.html'
    success_url = reverse_lazy('home')
    success_message = _('Workplace successfully deleted')
