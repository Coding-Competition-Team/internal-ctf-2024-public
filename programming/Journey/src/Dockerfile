FROM python:3.10

RUN apt update && \
    apt install -y socat

WORKDIR /app
COPY . .

CMD [ "socat", "tcp-listen:50000,fork,reuseaddr", "EXEC:'python3 /app/judge.py'" ]
