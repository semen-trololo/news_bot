import time
import parser
import requests
import mariadb


def connector(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL):
# Connect to MariaDB Platform
    while True:
        try:
            conn = mariadb.connect(
                user=USER_SQL,
                password=PASS_SQL,
                host=HOST_SQL,
                port=PORT_SQL,
                database=DB_SQL
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


def add_news(id_news, conn, cur):
    sql = "SELECT * FROM rss_news WHERE id_news = '{}';".format(id_news)
    cur.execute(sql)
    row = cur.fetchone()
    if row is None:
        status = status_url(id_news)
        flag_send = 0
        sql = "INSERT INTO rss_news (id_news, status, flag_send) VALUES ('{}', '{}', '{}');".format(id_news, status, flag_send)
        cur.execute(sql)
        conn.commit()


def start(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL):

    conn = connector(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL)
    cur = conn.cursor()
    _pda = parser.get_urls_pda()
    _3dnews = parser.get_urls_dnews()
    _opennet = parser.get_urls_opennet()
    _xaker = parser.get_urls_xakep()
    print('Get urls')
    for data in _pda:
        add_news(data, conn, cur)
    print('pda')
    for data in _3dnews:
        add_news(data, conn, cur)
    print('3dnews')
    for data in _opennet:
        add_news(data, conn, cur)
    print('opennet')
    for data in _xaker:
        add_news(data, conn, cur)
    print('xaker')
    print('Exit start')
    conn.close()
