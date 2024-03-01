from django.contrib import admin
from django.urls import path, include
import allauth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('players/', include('players.urls')),
    path('shop/', include('shop.urls')),
    path('users/', include('users.urls'))
    # path('accounts/', include(allauth.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

