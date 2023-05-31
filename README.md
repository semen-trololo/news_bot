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

#
FROM debian
RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip
RUN apt-get install -y libmariadb-dev
RUN apt-get install -y libmariadb-dev-compat
RUN apt-get install -y libmariadb3
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install pytelegrambotapi
RUN pip install "mariadb < 1.1"
ADD start.py /opt/
ADD bot.py /opt/
ADD parser.py /opt/
ADD settings.ini /opt/
CMD [ "python3", "/opt/bot.py" ]

#
version: '2'
services:
    mariadb:
        image: test.db
        container_name: db_news
        restart: always
        
    bot:
        image: parser_bot
        container_name: bot
        restart: always

