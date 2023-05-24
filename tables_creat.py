# Module Imports
# pip install mariadb
import mariadb
import time

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
        break
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        time.sleep(60)

# Get Cursor
cur = conn.cursor()
sql_send = """
CREATE TABLE rss_news(
   id_news VARCHAR(300) NOT NULL,
   status BOOL NOT NULL,
   flag_send BOOL NOT NULL,
   date DATE,
   PRIMARY KEY ( id_news )
   );
   """
cur.execute(sql_send)
conn.commit()
conn.close()
print('Creat table its OK...')
