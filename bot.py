import parser, start
import requests
import mariadb
import sys
import time


def add_news(id_news, conn):
    sql = "SELECT * FROM rss_news WHERE id_news = '{}';".format(id_news)
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    if row is None:
        status = start.status_url(id_news)
        flag_send = 0
        if status:
            flag_send = 1
        sql = "INSERT INTO rss_news (id_news, status, flag_send) VALUES ('{}', '{}', '{}');".format(id_news, status, flag_send)
        cur.execute(sql)
        conn.commit()
        print(id_news)

conn = start.connector()

while True:
    _pda = parser.get_urls_pda()
    _3dnews = parser.get_urls_dnews()
    _opennet = parser.get_urls_opennet()
    _xaker = parser.get_urls_xakep()
    for data in _pda:
        add_news(data, conn)
    for data in _3dnews:
        add_news(data, conn)
    for data in _opennet:
        add_news(data, conn)
    for data in _xaker:
        add_news(data, conn)
    time.sleep(360)
