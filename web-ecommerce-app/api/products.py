from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from products.models import Product, Category, ProductCategory
from stores.models import Store


class ProductPaginator(PageNumberPagination):
    page_size = 4
    max_page_size = 4


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = []
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class ProductCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ProductCategory
        exclude = []


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    # categories = CategorySerializer(many=True)
    categories = ProductCategorySerializer(many=True, source='categories_pivot')

    class Meta:
        model = Product
        exclude = []

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         exclude = []
#         depth = 1


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ProductPaginator
