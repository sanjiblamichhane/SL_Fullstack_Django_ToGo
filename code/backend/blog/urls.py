from django.urls import path 

from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
)


urlpatterns = [
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete'), # added by SL for new blog
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'), # added by SL for new blog
    path('new/', BlogCreateView.as_view(), name = 'post_new'), # added by SL for new blog
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='blog')
]
