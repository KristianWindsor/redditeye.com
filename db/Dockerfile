FROM mysql:8.0
ENV MYSQL_DATABASE redditeye
WORKDIR /

COPY ./src/ /docker-entrypoint-initdb.d/
COPY ./my.cnf /etc/mysql/conf.d/