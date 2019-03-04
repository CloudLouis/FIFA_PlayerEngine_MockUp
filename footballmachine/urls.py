from django.urls import path

from . import views

app_name = 'footballmachine'
urlpatterns= [
    path('', views.index, name="index"),
    path('search_result/', views.search_result, name="search_result"),
    path('builder_result/', views.builder_result, name="builder_result"),
    ]