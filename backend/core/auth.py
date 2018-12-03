# http://getblimp.github.io/django-rest-framework-jwt/
from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

auth_urlpatterns = [
    path("token-new/", obtain_jwt_token),
    path("token-refresh/", refresh_jwt_token),
    path("token-verify/", verify_jwt_token),
]
