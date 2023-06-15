CREATE TABLE rss_news(
   id_news VARCHAR(300) NOT NULL,
   link VARCHAR(300) NOT NULL,
   status BOOL NOT NULL,
   flag_send BOOL NOT NULL,
   date DATE,
   PRIMARY KEY ( id_news )
   );