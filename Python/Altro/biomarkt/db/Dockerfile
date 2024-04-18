FROM postgres:10-alpine
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
COPY init.sql  /docker-entrypoint-initdb.d/

