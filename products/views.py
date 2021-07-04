import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk):  # /api/products/<int:id>
        product = Product.objects.filter(id=pk).first()
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response({}, status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):  # /api/products/<int:id>
        product = Product.objects.filter(id=pk).first()
        if product is not None:
            serializer = ProductSerializer(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response({}, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):  # /api/products/<int:id>
        product = Product.objects.filter(id=pk).first()
        if product is not None:
            product.delete()
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response({}, status.HTTP_404_NOT_FOUND)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        if users.count() > 0:
            rand_user = random.choice(users)
            return Response({"id": rand_user.id})
        return Response({}, status.HTTP_404_NOT_FOUND)