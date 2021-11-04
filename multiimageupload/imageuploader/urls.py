from django.urls import path, include
from .views import upload, uploadImage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", upload),
    path("up", uploadImage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
