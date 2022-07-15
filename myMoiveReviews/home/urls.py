from django.urls import path 
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name = "home"),
    path('create', views.create, name ="create"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
]