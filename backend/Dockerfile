FROM python:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY ./src/ /app/
COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]