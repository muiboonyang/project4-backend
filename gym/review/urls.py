from django.urls import path
from . import views

urlpatterns = [
    path('view-all/', views.ReviewList.as_view()),  # get
    path('view/<str:pk>', views.ReviewDetail.as_view()),  # get
    path('create/', views.ReviewCreate.as_view()),  # post
    path('update/<str:pk>', views.ReviewUpdate.as_view()),  # post
    path('delete/<str:pk>', views.ReviewDelete.as_view()),  # delete
]
