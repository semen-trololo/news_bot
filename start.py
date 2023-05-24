import time
import xaker, dnews, pda, opennet
import requests
import mariadb
def connector():
# Connect to MariaDB Platform
    while True:
        try:
            conn = mariadb.connect(
                user="root",
                password="12345",
                host="127.0.0.1",
                port=3306,
                database="rss_feed"
            )
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            time.sleep(60)


def status_url(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print(False)
            return 0
        return 1
    except:
        return 0


def add_news(id_news, conn):
    sql = "SELECT * FROM rss_news WHERE id_news = '{}';".format(id_news)
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    if row is None:
        status = status_url(id_news)
        flag_send = 1
        sql = "INSERT INTO rss_news (id_news, status, flag_send) VALUES ('{}', '{}', '{}');".format(id_news, status, flag_send)
        cur.execute(sql)
        conn.commit()


conn = connector()
_pda = pda.parse()
_3dnews = dnews.parse()
_opennet = opennet.parse()
_xaker = xaker.parse()

for data in _pda:
    add_news(data, conn)
for data in _3dnews:
    add_news(data, conn)
for data in _opennet:
    add_news(data, conn)
for data in _xaker:
    add_news(data, conn)

conn.close()
