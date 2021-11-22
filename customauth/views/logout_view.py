import logging
from django.contrib.auth import logout
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


def logout_view(request):
    """ simple logout view """
    logger.info('logout view called')
    logout(request)
    return redirect('lms_login')
