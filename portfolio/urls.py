from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home ),
    path('download_res/', views.download_res),
    path('download_cover/', views.download_cover )
]
