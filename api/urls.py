from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from api import views

urlpatterns = [
  # path('auth/', include('rest_auth.urls')),
  path('', views.HelloView.as_view())
]