from flask import jsonify
from app.services.auth import system_authorize
from app.services.db_helper import get_stores_from_db


@system_authorize("admin")
def get_list_of_store_by_admin():
    # get store list
    store_list = get_stores_from_db()

    return jsonify({
        "message": "Success",
        "result": store_list,
    })
