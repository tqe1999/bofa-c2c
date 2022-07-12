FROM python:3.10.4-buster

WORKDIR /app
COPY ./swift_ingest/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./lib ./lib
COPY ./swift_ingest .

CMD [ "python", "-u", "main.py" ]