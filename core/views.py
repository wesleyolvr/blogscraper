from django.shortcuts import render
from .models import News
import sqlite3
   


def db_select():
    path = '/scraperNews/spiders/mynews.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = """
    SELECT Title
    FROM news
    """
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data