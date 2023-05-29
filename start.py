import time
import parser
import requests
import mariadb
import os
import configparser

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


def add_news(id_news, conn):
    sql = "SELECT * FROM rss_news WHERE id_news = '{}';".format(id_news)
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    if row is None:
        status = status_url(id_news)
        flag_send = 0
        sql = "INSERT INTO rss_news (id_news, status, flag_send) VALUES ('{}', '{}', '{}');".format(id_news, status, flag_send)
        cur.execute(sql)
        conn.commit()

def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        #create_config(path)
        pass
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    return value

path_settings = 'settings.ini'
PORT_SQL = get_setting(path_settings, 'sql', 'port')
HOST_SQL = get_setting(path_settings, 'sql', 'host')
USER_SQL = get_setting(path_settings, 'sql', 'user')
PASS_SQL = get_setting(path_settings, 'sql', 'password')
DB_SQL = get_setting(path_settings, 'sql', 'db')

conn = connector(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL)
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

conn.close()
