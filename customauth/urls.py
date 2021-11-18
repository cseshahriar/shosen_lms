from django.urls import path
from .views import LoginView, logout_view

app_name = 'customauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='lms_login'),
    path('login/', logout_view, name='lms_logout'),
]
