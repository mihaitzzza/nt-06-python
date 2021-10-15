from django.core import exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, viewsets
from rest_framework.response import Response

AuthUserModel = get_user_model()


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True)

    @staticmethod
    def validate_email(email):
        try:
            user = AuthUserModel.objects.get(email=email)
        except exceptions.ObjectDoesNotExist:
            user = None

        if user is not None:
            raise serializers.ValidationError('E-mail already taken.')

        return email

    def validate_password(self, password):
        temp_user = AuthUserModel(
            first_name=self.initial_data['first_name'],
            last_name=self.initial_data['last_name'],
            email=self.initial_data['email'],
        )

        validate_password(password, user=temp_user)

        return password

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        AuthUserModel.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )


class RegisterViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        register_serializer = RegisterSerializer(data=request.POST)

        if register_serializer.is_valid():
            register_serializer.create(register_serializer.validated_data)
            return Response({
                'message': f'User {register_serializer.validated_data["email"]} was successfully registered.'
            }, status=200)

        return Response({
            'errors': register_serializer.errors
        }, status=400)
