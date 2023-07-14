import string
from flask import jsonify
import re
import datetime
import time
from datetime import datetime, timedelta
import config


# from app.services.redis_helper import insert_user_session_and_grade_into_redis


def validate_msisdn(msisdn):
    for char in msisdn:
        if char not in string.digits:
            return False
    if len(msisdn) != 12:
        return False

    pattern = r'\b989\d{9}'
    result = re.findall(pattern, msisdn)
    if result is None:
        return False
    else:
        return True


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


def validate_msisdn(msisdn):
    for char in msisdn:
        if char not in string.digits:
            return False
    if len(msisdn) != 12:
        return False

    pattern = r'\b989\d{9}'
    result = re.findall(pattern, msisdn)
    if result is None:
        return False
    else:
        return True


USERS_SSO_ROLE_MAP = {
    "admin": "10",
    "merchant_user": "11",
    "merchant_admin": "12"

}

user_role_list = [
    {
        "id": "10",
        "name": "admin"
    },
    {
        "id": "11",
        "name": "merchant_user"
    },
    {
        "id": "12",
        "name": "merchant_admin"
    }
]
