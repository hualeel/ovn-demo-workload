FROM hualeel/python3_flask:latest
MAINTAINER Henry li

# 环境变量
ENV SERVICE_DIR=app

COPY . /$SERVICE_DIR
WORKDIR /$SERVICE_DIR
EXPOSE $SERVICE_PORT
CMD [ "python", "./main.py" ]