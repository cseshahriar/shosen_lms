from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from customauth.forms import LoginForm


class LoginView(View):
    """ Custom dashboard login view """
    template_name = 'admin/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        message = ''
        return render(
            request, 'admin/login.html',
            context={'form': form, 'message': message}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['passwordusername'],
            )
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('dashboard')
            message = 'Login failed! User must be an active or staff user'
        return render(
            request,
            'admin/login.html',
            context={'form': form, 'message': message}
        )
