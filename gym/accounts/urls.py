from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView, )
from . import views

# TokenObtainPairView,

urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CreateUser.as_view(), name='create_user'),
]
