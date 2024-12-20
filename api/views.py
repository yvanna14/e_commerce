from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Products, Orders, Reviews
from .serializers import UsersSerializer, ProductsSerializer, OrdersSerializer, ReviewsSerializer

# Create your views here.
class UserView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):

    def get(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            serializer = UsersSerializer(user)
            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            serializer = UsersSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):

    def get(self, request, pk):
        try:
            product = Products.objects.get(pk=pk)
            serializer = ProductsSerializer(product)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            product = Products.objects.get(pk=pk)
            serializer = ProductsSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            product = Users.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OrdersView(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class OrdersDetailView(APIView):

    def get(self, request, pk):
        try:
            order = Orders.objects.get(pk=pk)
            serializer = OrdersSerializer(order)
            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            order = Orders.objects.get(pk=pk)
            serializer = OrdersSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            order = Orders.objects.get(pk=pk)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ReviewsView(APIView):
    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ReviewsDetailView(APIView):

    def get(self, request, pk):
        try:
            review = Reviews.objects.get(pk=pk)
            serializer = ReviewsSerializer(review)
            return Response(serializer.data)
        except Reviews.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            review = Reviews.objects.get(pk=pk)
            serializer = ReviewsSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reviews.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            review = Users.objects.get(pk=pk)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Reviews.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

def signin(request):
    return render(request, 'signin.html')