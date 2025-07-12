from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsAdminOrReadOnly]

class ProoductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

