from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', CustomUserViewSet, basename='users')


urlpatterns = [
    path(r'accounts/', include((router.urls, 'accounts'))),
    path(r'accounts/register',RegisterNewUser.as_view({'post':'create'}), name='register_user'),
    path(r'accounts/token', TokenObtainPairViewCustom.as_view(), name='token_obtain_pair'),
    path(r'accounts/token/refresh', TokenRefreshViewCustom.as_view(), name='token_refresh'),

]