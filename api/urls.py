from django.urls import path

from api import views

urlpatterns = [
    # path('auth/', include('rest_auth.urls')),
    path('', views.HelloView.as_view()),
    path('region/<int:pk>', views.RegionDetailView.as_view()),
    path('check-code', views.CheckCodeView.as_view()),
    path('disease-list', views.DiseaseListView.as_view()),
    path('check-item-list', views.CheckItemListView.as_view()),
    path('check-user-detail', views.CheckUserDetail.as_view()),
    path('check-report-detail', views.CheckReportDetail.as_view()),
    path('login', views.LoginView.as_view())
]
