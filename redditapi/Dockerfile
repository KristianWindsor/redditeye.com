FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
	apt-get install -y telnet

COPY ./src/ /app/
COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]