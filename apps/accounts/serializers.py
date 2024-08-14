from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    RefreshToken,
)

from .models import *
from .services import make_username

class RegisterNewUserSerializer(serializers.Serializer):
    # TODO - Aplicar internacionalização (translation)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, write_only=True)

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("This email is already in use."))
        return value

    @transaction.atomic
    def create(self, validate_data, **kwargs):
        self.gen_password = CustomUser.objects.make_random_password()
        username = make_username(validate_data['name'])

        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError(_('Username already exists.'))

        user = CustomUser.objects.create(
            username=username,
            password=make_password(self.gen_password),
            email=validate_data['email'],
            is_first_login = True
        )

        return user
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'password': self.gen_password
        }

class TokenObtainPairSerializerCustom(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        # Retorna informações do usuário juntamente com os tokens
        serializer = TokenUserSerializer(self.user)
        data['user'] = serializer.data
        return data

class TokenUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_first_login = serializers.BooleanField(read_only=True)
    email = serializers.EmailField(read_only=True)
    
class RegisterNewUserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()

class TokenResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = TokenUserSerializer()