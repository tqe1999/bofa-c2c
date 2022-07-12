FROM python:3.10.4-buster

WORKDIR /app
COPY ./api/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./lib ./lib
COPY ./api .

CMD [ "python", "-u", "main.py" ]