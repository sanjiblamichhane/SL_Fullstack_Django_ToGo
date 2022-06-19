
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name = 'home.html')),
    path('home/', TemplateView.as_view(template_name = 'home.html')),
    path('blog/', include('blog.urls')), ## added by SL for Blog App
    path('accounts/', include('django.contrib.auth.urls')), ## added by SL for User Authentication
    path('', include('pages.urls')), ## url for posts app
]

urlpatterns += staticfiles_urlpatterns()
