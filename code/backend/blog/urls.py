from django.urls import path 

from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'), # added by SL for new blog
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='blog')
]
