import parser, start
import time
import configparser
import os
import telebot
import logging
# pip install pytelegrambotapi


def send_teleg_bot(message):
    try:
        bot.send_message(chat_id=id_chat, text=message)
        time.sleep(1)
    except:
        py_logger.warning('Error send message in telegram')

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

def add_news(id_news, conn, cur):
    sql = "SELECT * FROM rss_news WHERE id_news = '{}';".format(id_news)
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
        send_teleg_bot(id_news)
        time.sleep(1)

py_logger = logging.getLogger('[BOT]')
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler('news_bot.log', mode='a')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

path_settings = '/opt/settings.ini'
PORT_SQL = int(get_setting(path_settings, 'sql', 'port'))
HOST_SQL = get_setting(path_settings, 'sql', 'host')
USER_SQL = get_setting(path_settings, 'sql', 'user')
PASS_SQL = get_setting(path_settings, 'sql', 'password')
DB_SQL = get_setting(path_settings, 'sql', 'db')
_KEY = get_setting(path_settings, 'telegram', 'key')
id_chat = get_setting(path_settings, 'telegram', 'id_chat')

bot = telebot.TeleBot(_KEY)

send_teleg_bot('Start news bot...')
py_logger.info('Start news bot...')

start.start(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL, py_logger)

while True:
    conn = start.connector(USER_SQL, PASS_SQL, HOST_SQL, PORT_SQL, DB_SQL)
    cur = conn.cursor()
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
    print('[*] Step..')
    conn.close()
    time.sleep(300)
