from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="english_news"),
    path('hindi/',views.hindi_news,name="hindi_news")
]
