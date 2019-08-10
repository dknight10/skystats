from json.decoder import JSONDecodeError

import requests
from django.conf import settings
from functools import wraps
from jose import jwt
from rest_framework.request import Request

from rest_framework import response, status


class AuthError(Exception):
    """Error when using Auth0 jwts"""


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """

    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[1])
            unverified_claims = jwt.get_unverified_claims(token)
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return f(*args, **kwargs)
            return response.Response(
                {"message": "You don't have access to this resource"},
                status=status.HTTP_403_FORBIDDEN,
            )

        return decorated

    return require_scope


def get_email_from_user_info(request: Request) -> str:
    jwt = get_token_auth_header(request)

    user_info = requests.get(
        settings.AUTH0_URL + "userinfo", headers={"Authorization": f"Bearer {jwt}"}
    )
    try:
        return user_info.json()["email"]
    except (KeyError, JSONDecodeError):
        raise AuthError("Could not fetch userinfo")
