from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    # path('auth/', include('rest_auth.urls')),
    path('', views.HelloView.as_view()),
    path('region/<int:pk>', views.RegionDetailView.as_view()),
    path('check-code', views.CheckCodeView.as_view())
]
