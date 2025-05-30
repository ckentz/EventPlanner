from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
]
