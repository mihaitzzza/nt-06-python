import graphene
import graphql_jwt
from products.models import Product
from graphqlapi.types import ProductType
# from graphqlapi.mutations import CreateProduct, RegisterUser
from graphqlapi.mutations import CreateProduct, RegisterUserModel
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):
    message = graphene.String(default_value="Good bye, World!")
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, p_id=graphene.Int())

    @staticmethod
    @login_required
    def resolve_message(root, info):
        # return 'Hey, this is from resolver!'
        return None

    @staticmethod
    def resolve_products(root, info):
        return Product.objects.all()

    @staticmethod
    def resolve_product(root, info, p_id):
        try:
            product = Product.objects.get(pk=p_id)
        except Product.DoesNotExist:
            product = None

        return product


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    # register = RegisterUser.Field()
    register = RegisterUserModel.Field()

    create_product = CreateProduct.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
