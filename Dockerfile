FROM alpine:latest

MAINTAINER A M Hendley <amhendley@gmail.com>

RUN apk add gcc musl-dev python3 python3-dev
RUN mkdir /app

COPY app/* /app/
COPY requirements.txt /app/

WORKDIR app

RUN pip3 install -r requirements.txt

EXPOSE 9000

#CMD ["python3", "/app/run_managed.py"]
CMD ["gunicorn","-b","0.0.0.0:9000","-w","3","-k","gevent","--log-file","-","--log-level","debug","--access-logfile","-","launch:app"]
