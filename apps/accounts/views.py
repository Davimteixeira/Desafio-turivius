from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework import permissions, status, viewsets, mixins
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
    Cadastra novo usuário na plataforma. 
    """
    serializer_class = RegisterNewUserSerializer

@method_decorator(name='post', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: TokenResponseSerializer}
))
class TokenObtainPairViewCustom(TokenObtainPairView):
    """ 
    Autentica o usuário na plataforma através de suas credenciais de acesso.
    
    """
    permission_classes =[permissions.AllowAny,]
    serializer_class = TokenObtainPairSerializerCustom


class TokenRefreshViewCustom(TokenRefreshView):
    """
    Atualiza token de acesso. Quando o access token é expirado, este endpoint deve ser utilizado
    para realizar a atualização do token e manter o usuário autenticado.
    """
    pass
