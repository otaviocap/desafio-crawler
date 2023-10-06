FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/src/"
ENV OS_ENV "container"

COPY . /app

CMD [ "python3", "/app/src/app.py", "--csv", "--json" ]