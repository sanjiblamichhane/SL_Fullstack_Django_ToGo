from django.urls import path 

from .views import HomePageView, AccountPageView, BlogPageView

urlpatterns = [
    path('account/', AccountPageView.as_view(), name='account'), ## added by SL
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    
]
