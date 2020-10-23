from django.urls import path
from .views import SignUpView

from .import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit/', views.dashboard_edit, name='dashboard_edit'),
]