FROM python:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/

COPY ./backend/ /usr/src/app/
COPY requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/src/app/app.py"]