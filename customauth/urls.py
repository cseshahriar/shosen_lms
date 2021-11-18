from django.urls import path
from .views import LoginView

app_name = 'customauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='lms_login'),
]
