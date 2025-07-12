from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users, extra check in logic if needed

class ProoductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]  # Required for all actions

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 2:
            return ProductReview.objects.all()
        raise PermissionDenied("Only admins can view product reviews.")

    def perform_create(self, serializer):
        # Allow any logged-in user to create review
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return super().get_permissions()


