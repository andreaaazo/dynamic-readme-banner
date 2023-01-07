from django.urls import path
from .views import TextRenderer

urlpatterns = [
    path("", TextRenderer.as_view(), name="home"),
]
