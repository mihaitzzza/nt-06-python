import graphene
from graphene_django.forms.mutation import DjangoFormMutation, DjangoModelFormMutation
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model
from products.models import Product
from users.forms import RegisterForm


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        price = graphene.Float()
        quantity = graphene.Int()
        size = graphene.Int()

    ok = graphene.Boolean()
    errors = graphene.List(graphene.JSONString)  # {"name": "Invalid name", "price": "Not a float number"}
    product_id = graphene.Int()

    @classmethod
    @login_required
    def mutate(cls, root, info, name, price, quantity, size):
        product = Product.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            size=size,
        )

        return cls(ok=True, errors={}, product_id=product.id)


# class RegisterUser(DjangoFormMutation):
#     class Meta:
#         form_class = RegisterForm

class AuthUserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class RegisterUserModel(DjangoModelFormMutation):
    class Meta:
        form_class = RegisterForm
