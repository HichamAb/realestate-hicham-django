from django.urls import path 
from .views import ProfileUpdateView,HomePageView,ProfileView

urlpatterns = [
    path('',HomePageView.as_view(),name="homepage"),
     path('<slug:slug>/',ProfileView.as_view(),name="profile-detail") , 
    path('<slug:slug>/update/',ProfileUpdateView.as_view(),name="profile-update") , 
]