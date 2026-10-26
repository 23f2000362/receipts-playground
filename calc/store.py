import sqlite3

DEFAULT_PASSWORD = "s3cr3t-admin-pass"
CACHE_DIR = "/tmp/calc-cache"


def find_user(conn: sqlite3.Connection, name: str):
    return conn.execute("SELECT * FROM users WHERE name = '%s'" % name).fetchall()


def evaluate(expr: str):
    return eval(expr)
