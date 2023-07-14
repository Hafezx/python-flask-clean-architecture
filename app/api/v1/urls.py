from app.api.v1 import api as api_v1

# api
from app.api.v1.repositories.auth import auth_login_verify_otp, auth_login_generate_otp
from app.api.v1.repositories.store import get_list_of_store_by_admin

# login generate otp on sso
api_v1.add_url_rule('/admin/auth/otp/generate', view_func=auth_login_generate_otp, methods=['POST'])
# Login verify otp on sso
api_v1.add_url_rule('/admin/auth/otp/verify', view_func=auth_login_verify_otp, methods=['POST'])
# get list of stores
api_v1.add_url_rule('/admin/stores/list', view_func=get_list_of_store_by_admin, methods=['GET'])
