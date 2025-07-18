from rest_framework import serializers
from .models import Product, ProductReview

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'
        fields = ['id', 'product', 'user', 'rating_star', 'rating_desc', 'created_at']
