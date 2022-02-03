from django.urls import path
from . import views

urlpatterns = [
    path('view-all/', views.PersonalDetailsAll.as_view()),  # get
    path('view/<str:pk>', views.PersonalDetailsOne.as_view()),  # get
    path('create/', views.PersonalDetailsCreate.as_view()),  # post
    path('update/<str:pk>', views.PersonalDetailsUpdate.as_view()),  # post
    path('delete/<str:pk>', views.PersonalDetailsDelete.as_view()),  # delete
]
