from django.contrib import admin
from django.urls import path, include
from users.views import register_view
from . import views


urlpatterns = [
    path('http_response/', views.http_response),
    path('html_response/', views.html_response),
    path('posts/', views.post_list_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('posts/post_create/', views.post_create_view),
    path('posts/<int:post_id>/post_create/', views.comment_create_view),
    path('users/register/', register_view),
]
