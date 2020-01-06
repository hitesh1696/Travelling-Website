from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from travello import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('travello.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/destinations/', include('travello.api.urls')),





]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)