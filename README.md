# news_bot

docker run --detach --name db --env MARIADB_ROOT_PASSWORD=12345 -p 3306:3306 mariadb:latest 

FROM mariadb:latest

COPY test.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD admin
ENV MYSQL_DATABASE test
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD admin

EXPOSE 3306
Тест.sql:

CREATE TABLE IF NOT EXISTS test (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(32) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO test (name) VALUES
('Toto'),
('Jack'),
('Titi');