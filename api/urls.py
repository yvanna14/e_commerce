from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('Orders/', views.OrdersView.as_view()),
    path('Orders/<int:pk>/', views.OrdersView.as_view()),
    path('Reviews/', views.ReviewsView.as_view()),
    path('shops/<int:pk>/', views.ReviewsView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('/signin', views.signin, name='signin')
]