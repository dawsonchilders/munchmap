from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('restaurants/', views.restaurant_index, name='index'),
  path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name='detail'),
  path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
  path('accounts/signup', views.signup, name='signup'),

]