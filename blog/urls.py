from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    path('new/',views.post_new),
    path('restaurants/', views.restaurants_list),
    path('restaurants/<int:pk>/',views.rest_post_page),
    path('restaurants/new/', views.rest_new),
]
