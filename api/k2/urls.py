from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.top),
    path('about/', views.about),
    path('hello/', views.index),
]
