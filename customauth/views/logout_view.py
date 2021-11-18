from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    """ simple logout view """
    logout(request)
    # redirect to
    return redirect('lms_login')
