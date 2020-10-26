from django.urls import path

from .import views
from .views import PostView


urlpatterns = [
    path('', PostView.as_view()),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]