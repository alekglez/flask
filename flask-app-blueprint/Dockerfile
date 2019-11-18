FROM python:3.7-alpine
LABEL maintainer = "Alejandro Cora Gonzalez <alek.cora.glez@gmail.com>"

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev git && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

#ADD . /flask-app
#WORKDIR /flask-app
#RUN pip install -r requirements/base.txt
#ENTRYPOINT ["./entrypoint.sh"]

RUN git clone --branch develop https://github.com/alekglez/flask.git /flask-app
RUN pip install -r /flask-app/flask-app-blueprint/requirements/base.txt
CMD chmod +x flask-app/flask-app-blueprint/entrypoint.sh
#COPY ~/flask-app/flask-app-blueprint/entrypoint.sh /usr/local/bin/
#RUN ln -s /usr/local/bin/entrypoint.sh

ENTRYPOINT ["flask-app/entrypoint.sh"]
EXPOSE 5000
