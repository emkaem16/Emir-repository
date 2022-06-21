import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY, username TEXT,"
               "photo TEXT, name TEXT, surname TEXT,"
               "age INTEGER, region TEXT)")
    db.commit()