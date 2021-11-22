from django.urls import path
from .views import LMSLoginView, logout_view, DashboardView

urlpatterns = [
    # authentication urls
    path('login/', LMSLoginView.as_view(), name='lms_login'),
    path('logout/', logout_view, name='lms_logout'),

    # dashboard urls
    path('dashboard/', DashboardView.as_view(), name='lms_dashboard'),
]
