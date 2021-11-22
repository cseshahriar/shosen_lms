import logging
from django.views import View
from django.shortcuts import render, redirect  # noqa
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    """ Dashboard view """

    template_name = 'adminpanel/dashboard.html'
    login_url = '/lms/login/'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get(self, request, *args, **kwargs):
        logger.info('Dashboard get method called')
        context = {}
        return render(request, self.template_name, context)
