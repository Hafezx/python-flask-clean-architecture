# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
import config
# connect mysql connection
from app.logger import ms_error_logger
from app.services.app_exceptions import CustomException


def db_connector(database_name=config.MYSQL_DATABASE):
    try:
        connection = mysql.connector.connect(host=config.MYSQL_HOST, user=config.MYSQL_USERNAME,
                                             password=config.MYSQL_PASSWORD,
                                             database=database_name,
                                             connection_timeout=2
                                             )
        if connection.is_connected():
            return connection
        else:
            raise Exception("can not connect to db")
    except Exception as e:
        ms_error_logger(response_code=217002, message="DB error. Error is:{}".format(e), action="DB_CONNECTION")
        raise CustomException("Please Try Again", 422)


def execute_query(query, query_data=None, data=None, connection=None, cursor=None, close_con=True,
                  database_name=config.MYSQL_DATABASE):
    if connection is None and cursor is None:
        connection, cursor = open_db_connection(database_name)

    if query_data:
        cursor.execute(query, query_data)
    else:
        cursor.execute(query)
    result = None
    if data is not None:
        if data == "lastrowid":
            result = cursor.lastrowid
        elif data == "one":
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
    if close_con:
        commit_and_close_db_connection(connection, cursor)
    if result is not None:
        return result


def open_db_connection(database_name):
    connection = db_connector(database_name)
    cursor = connection.cursor(dictionary=True)
    return connection, cursor


def commit_and_close_db_connection(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()

def get_stores_from_db():
    query = '''SELECT * FROM merchant'''
    try:
        resp = execute_query(query, data='all')
    except Exception:
        raise CustomException("Failed to get data", 406)

    return resp
