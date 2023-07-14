from functools import wraps
from flask import request, g
from app.services.app_exceptions import AuthenticationException, PermissionDeniedException
from app.services.token_helper import decode_token


def system_authorize(permission="no_permission"):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                if 'Authorization' not in request.headers or len(request.headers.get('Authorization')) < 10:
                    raise AuthenticationException()
            except Exception:
                raise AuthenticationException()

            g.user_type = request.headers.get("user_type", None)

            try:
                #  validate user token and get user msisdn
                user_mobile_number, user_id = decode_token(request.headers.get('Authorization'))
                g.user_id = user_id
                g.user_mobile_number = user_mobile_number
            except Exception as e:
                print("auth err: ", e)
                raise AuthenticationException()

            if not check_access(permission):
                raise PermissionDeniedException()

            return function(*args, **kwargs)

        return wrapper

    return inner_function


def check_access(permission):
    permissions = g.user_roles
    if "admin" in permissions:
        return True
    required_permission_list = permission.split(',')
    for item in required_permission_list:
        if item in permissions:
            return True
    return False
