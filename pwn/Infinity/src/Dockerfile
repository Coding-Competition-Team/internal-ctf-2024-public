FROM ubuntu:22.04@sha256:f9d633ff6640178c2d0525017174a688e2c1aef28f0a0130b26bd5554491f0da

RUN apt update && \
    apt install -y socat python3

WORKDIR /app
COPY . .

RUN chmod 644 /app/flag.txt
RUN chmod 744 /app/main.py 

EXPOSE 5000

CMD ["socat", "tcp-listen:5000,fork,reuseaddr", "EXEC:'python3 /app/main.py'"]