from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "sites"

urlpatterns = [
    path('', views.main, name = "main"),
    path('ideacreate', views.ideacreate, name = "ideacreate"),
    path('idea/<int:id>', views.ideadetail, name = "ideadetail"),
    path('ideaupdate/<int:id>', views.ideaupdate, name = "ideaupdate"),
    path('ideadelete/<int:id>', views.ideadelete, name = "ideadelete"),
    path('devtlist', views.devtlist, name="devtlist"),
    path('devtcreate', views.devtcreate, name = "devtcreate"),
    path('devtdetail/<int:id>', views.devtdetail, name = "devtdetail"),
    path('devtupdate/<int:id>', views.devtupdate, name = "devtupdate"),
    path('devtdelete/<int:id>', views.devtdelete, name = "devtdelete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)