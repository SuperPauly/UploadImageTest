from django.urls import path, include
from .views import upload, uploadImage

urlpatterns = [
    path("", upload),
    path("up", uploadImage),
]
