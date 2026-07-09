from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'post/<int:post_id>/', views.post_detail, name='post_detail'),
    path(r'post/new/', views.post_new, name='post_new'),
    path(r'post/edit/<int:post_id>/', views.post_edit, name='post_edit'),
]