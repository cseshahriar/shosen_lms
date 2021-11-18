from django.views import View
from django.shortcuts import render, redirect  # noqa
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class DashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    """ Dashboard view """

    template_name = 'admin/dashboard.html'

    def test_func(self):
        """ superuser and staff can access dashboard """
        return self.request.user.is_staff or self.request.user.is_staff

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
