FROM python:3.7-alpine
LABEL maintainer = "Alejandro Cora Gonzalez <alek.cora.glez@gmail.com>"

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev git && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

# ADD . /flask-app
# WORKDIR /flask-app
# RUN pip install -r requirements/base.txt
# ENTRYPOINT ["./entrypoint.sh"]

ENV APP_PATH=/home/flask-app
RUN mkdir $APP_PATH

RUN addgroup -S flask && adduser -S flask -G flask
RUN chown -R flask:flask $APP_PATH
WORKDIR $APP_PATH

RUN git clone --branch develop https://github.com/alekglez/flask.git $APP_PATH
RUN pip install -r $APP_PATH/flask-app-blueprint/requirements/base.txt
#CMD chmod +x $APP_PATH/flask-app-blueprint/entrypoint.sh

USER flask
#ENTRYPOINT ["/home/flask-app/flask-app-blueprint/entrypoint.sh"]
EXPOSE 5000
