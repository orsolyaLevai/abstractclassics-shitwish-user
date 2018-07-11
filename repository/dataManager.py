import os
import psycopg2
import psycopg2.extras
import urllib.parse as urlparse

def get_connection_string():
    url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
    connection_string = "dbname=%s user=%s password=%s host=%s " % (
        url.path[1:], url.username, url.password, url.hostname)
    return connection_string


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        # we set the cursor_factory parameter to return with a RealDictCursor cursor (cursor which provide dictionaries)
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper

