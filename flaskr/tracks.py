import functools

from flask import Blueprint, g
import mysql.connector
import os

bp = Blueprint('tracks', __name__, url_prefix='/tracks')

@bp.before_app_request
def load_db():
    MYSQL_PWD = os.getenv('MYSQL_PWD')
    print(MYSQL_PWD)

    g.db = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MYSQL_PWD,
        database='spotify_toolkit'
    )
    g.cursor = g.db.cursor()

@bp.route('/<int:track_id>', methods=['GET'])
def get_by_id(track_id: int):
    g.cursor.execute('SELECT * FROM tracks WHERE id = %s', [track_id])

    print(g.cursor.fetchall())
    return str(track_id)