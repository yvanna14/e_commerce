from rest_framework import serializers
from .models import Users, Products, Orders, Reviews

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'profile_picture']

        extra_kwargs = {'password': {'write_only': True}}

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'stock',  'product_picture']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'name', 'orderedBy', 'orderDate']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'