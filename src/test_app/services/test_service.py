import sqlite3

def return_hello():
    return "Hello"


def db():
    conn = sqlite3.connect("data/test.db")
    return conn.cursor()