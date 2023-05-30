# news_bot


FROM mariadb:latest

COPY test.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD 12345
ENV MYSQL_DATABASE rss_feed
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD admin

EXPOSE 3306
# test.sql:

CREATE TABLE rss_news(
   id_news VARCHAR(300) NOT NULL,
   status BOOL NOT NULL,
   flag_send BOOL NOT NULL,
   date DATE,
   PRIMARY KEY ( id_news )
   );
#
docker build -t test.db .
docker run --detach --name db -p 3306:3306
docker run --detach --name db  -p 3306:3306 test.db
