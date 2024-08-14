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
    
class RegisterNewUserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    