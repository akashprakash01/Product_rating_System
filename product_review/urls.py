"""
URL configuration for product_review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.decorators import api_view
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from products.views import ProductViewSet, ProoductReviewViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_reviews', ProoductReviewViewSet)


@api_view(['GET'])
def custom_api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'product_reviews': reverse('productreview-list', request=request, format=format),
        'login': request.build_absolute_uri('/api/login/')    })
urlpatterns = [
   path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
    path('api/login/', obtain_auth_token),  
]

