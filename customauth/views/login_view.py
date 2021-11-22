import logging
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from customauth.forms import LMSLoginForm

logger = logging.getLogger(__name__)


class LMSLoginView(View):
    templates = 'adminpanel/login.html'
    form_class = LMSLoginForm

    def get(self, request):
        context = {"form": self.form_class}
        return render(request, self.templates, context)

    def post(self, request):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect(self.get_success_url())
            else:
                messages.warning(
                    self.request,
                    "Invalid Username Or Password"
                )
                context = {"form": self.form_class}
                return render(request, self.templates, context)
        else:
            messages.warning(self.request, "Invalid Data")
            context = {"form": self.form_class}
            return render(request, self.templates, context)

    def get_success_url(self):
        messages.success(self.request, "Login successfully!")
        logger.debug("Login successfully")
        return reverse_lazy("lms_dashboard")
