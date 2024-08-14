from datetime import datetime

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from django.dispatch import receiver
from rest_framework import viewsets, mixins


from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import permissions, status, viewsets, mixins
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



from .models import *
from .serializers import *

@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: RegisterNewUserResponseSerializer}
))
class RegisterNewUser(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Cadastra novo usuário na plataforma. O campo tipo representa o perfil do usuário, sendo:
    - 1: Administrador
    - 2: Funcionário
    - 3: Gestor de Contas
    - 4: Prestador
    - 5: Prestador ADM

    **Nota:** Este endpoint não permite o cadastro de usuários do tipo **funcionário**.
    Perfis de usuário do tipo Administrador não precisam enviar o campo company_id, enquanto os
    demais perfis sim, caso contrário, um erro será retornado.
    """
    serializer_class = RegisterNewUserSerializer

