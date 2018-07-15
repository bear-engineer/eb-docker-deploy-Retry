FROM            python:3.6.5-slim
MAINTAINER      d.sehyeon@gmail.com

RUN             apt -y update && apt -y dist-upgrade
RUN             apt -y install build-essential
RUN             apt -y install nginx supervisor


# local requirements.txt file 을 /srv 에 복사 후 pip install 실행
COPY            ./requirements.txt  /srv/
RUN             pip install -r /srv/requirements.txt

# production
ENV             BUILD_MODE      production
ENV             DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY            .   /srv/project


RUN             cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf \
                        /etc/nginx/nginx.conf && \
                cp -f   /srv/project/.config/${BUILD_MODE}/nginx_app.conf \
                        /etc/nginx/sites-available/ && \
                rm -f   /etc/nginx/sites-enabled/* && \
                ln -sf  /etc/nginx/sites-available/nginx_app.conf \
                        /etc/nginx/sites-enabled/

RUN             cp -f   /srv/project/.config/${BUILD_MODE}/supervisor_app.conf \
                        /etc/supervisor/conf.d/

CMD             supervisord -n
