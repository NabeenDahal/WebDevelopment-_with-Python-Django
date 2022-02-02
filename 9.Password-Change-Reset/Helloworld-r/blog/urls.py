#blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogs , name='blogs'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/blog_create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<int:pk>/edit/',views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blogs/<int:pk>/delete/',views.BlogDeleteView.as_view(), name='blog_delete'), # new
]