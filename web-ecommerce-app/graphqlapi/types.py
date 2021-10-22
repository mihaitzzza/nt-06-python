# import graphene
#
#
# class CategoryType(graphene.ObjectType):
#     id = graphene.Int()
#     name = graphene.String()
#
#
# class ProductCategoryType(graphene.ObjectType):
#     id = graphene.Int()
#     # category = graphene.Field(CategoryType, cId=graphene.Int())
#     # product = graphene.Field('ProductType', pId=graphene.Int())
#     extra_column = graphene.Int()
#
#
# class ProductType(graphene.ObjectType):
#     id = graphene.Int()
#     name = graphene.String()
#     price = graphene.Float()
#     color = graphene.String()
#     size = graphene.String()
#     currency_price = graphene.String()
#     categories = graphene.List(CategoryType)
#     categories_pivot = graphene.List(ProductCategoryType)
#
#     def resolve_currency_price(self, info):
#         return '%.2f RON' % self.price
#
#     def resolve_categories(self, info):
#         return self.categories.all()
#
#     def resolve_categories_pivot(self, info):
#         return self.categories_pivot.all()

#########################################################################
#### Django functionality mapping #######################################
#########################################################################

import graphene
from graphene_django import DjangoObjectType
from products.models import Product, Category, ProductCategory


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        exclude = []


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory
        exclude = []


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        exclude = []  # or fields = [...]

    currency_price = graphene.String()

    def resolve_currency_price(self, info):
        return '%.2f RON' % self.price
