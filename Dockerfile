FROM ubuntu:18.04
WORKDIR /app
COPY requirements.txt ./
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
COPY . .
ENV GUNICORN_CMD_ARGS --bind=0.0.0.0
EXPOSE 8000
ENTRYPOINT ["gunicorn", "Endpoint:app"]
