from django.urls import path
from .views import LoginView, logout_view, DashboardView

app_name = 'customauth'

urlpatterns = [
    # authentication urls
    path('login/', LoginView.as_view(), name='lms_login'),
    path('login/', logout_view, name='lms_logout'),

    # dashboard urls
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
