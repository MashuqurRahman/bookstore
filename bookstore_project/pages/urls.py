from django.contrib import admin
from django.urls import path,include
from .views import HomePageView,AboutPageView

urlpatterns = [
   
    path('',HomePageView,name="home"),
    path('about',AboutPageView,name="about")
]
