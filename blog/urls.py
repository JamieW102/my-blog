from django.urls import path, include
from . import views
from django.contrib import admin

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

#from django.contrib.auth import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.post_list, name='post_list'),
    path('gallery', views.gallery, name='gallery'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/posts'), name='logout'),
]
