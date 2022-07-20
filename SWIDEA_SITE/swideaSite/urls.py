from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "sites"

urlpatterns = [
    path('', views.main, name = "main"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)