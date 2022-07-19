from django.urls import path
from . import views

urlpatterns = [
    path('view-all/', views.PersonalDetailsAll.as_view()),  # get
    path('view/<str:fk>', views.PersonalDetailsOne.as_view()),  # get
    path('create/', views.PersonalDetailsCreate.as_view()),  # post
    path('update/<str:fk>', views.PersonalDetailsUpdate.as_view()),  # post
    path('delete/<str:fk>', views.PersonalDetailsDelete.as_view()),  # delete
]
