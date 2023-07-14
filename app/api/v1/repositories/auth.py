from flask import request
import json

from app.services.app_exceptions import InputValidationError, CustomException


def auth_login_generate_otp():
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException("Bad request:{}".format(e), 406)

    if 'mobile' not in req_data:
        raise InputValidationError()
    mobile = req_data['mobile']
    return {"Call your generate otp function"}(mobile)


def auth_login_verify_otp():
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException("Bad request:{}".format(e), 406)

    if 'mobile' not in req_data or 'otp' not in req_data:
        raise InputValidationError()
    mobile = req_data['mobile']
    otp = req_data['otp']

    return {"Add your verify OTP function and return user a token"}(user_mobile=mobile, user_otp=otp)
