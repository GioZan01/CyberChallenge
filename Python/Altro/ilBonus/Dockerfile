FROM composer as deps
ADD ./composer.json  /app/
RUN composer install --ignore-platform-reqs --no-scripts


FROM php:7-fpm
RUN pecl install mongodb
RUN echo "extension=mongodb.so" >> /usr/local/etc/php/conf.d/mongodb.ini
ADD ./ /var/www/html/
COPY --from=deps /app/vendor/ /var/www/html/vendor/
