
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), ## added by SL for Blog App
    path('', include('pages.urls')), ## url for posts app
]
