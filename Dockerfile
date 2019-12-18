FROM python:3.6-alpine
RUN apk add build-base



pip3 install uwsgi

ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
