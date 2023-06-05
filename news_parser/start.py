import time
import parser
import requests
import mariadb


def connector(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL, py_logger):
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
            py_logger.warning(f"Error connecting to MariaDB Platform: {e}")
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


def start(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL, py_logger):

    conn = connector(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL, py_logger)
    cur = conn.cursor()
    while True:
        _pda, _pda_error = parser.get_urls_pda(py_logger)
        _3dnews, _3dnews_error = parser.get_urls_dnews(py_logger)
        _opennet, _opennet_error = parser.get_urls_opennet(py_logger)
        _xaker, _xaker_error = parser.get_urls_xakep(py_logger)
        if _pda_error:
            for data in _pda:
                add_news(data, conn, cur)
        if _3dnews_error:
            for data in _3dnews:
                add_news(data, conn, cur)
        if _opennet_error:
            for data in _opennet:
                add_news(data, conn, cur)
        if _xaker_error:
            for data in _xaker:
                add_news(data, conn, cur)
        if _xaker_error and _opennet_error and _pda_error and _3dnews_error:
            break
    py_logger.info('Exit start')
    conn.close()
