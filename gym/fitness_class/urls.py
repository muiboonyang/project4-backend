from django.urls import path
from . import views

urlpatterns = [
    path('view-all/', views.ClassList.as_view()),  # get
    path('view/<str:pk>', views.ClassDetail.as_view()),  # get
    path('create/', views.ClassCreate.as_view()),  # post
    path('update/<str:pk>', views.ClassUpdate.as_view()),  # post
    path('delete/<str:pk>', views.ClassDelete.as_view()),  # delete
]
