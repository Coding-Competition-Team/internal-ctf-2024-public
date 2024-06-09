FROM python:3.10

RUN apt update && \
    apt install -y socat

WORKDIR /app
COPY . .

RUN chmod 644 /app/flag.txt
RUN chmod 744 /app/slightslant.py 

EXPOSE 7022

CMD [ "socat", "tcp-listen:7022,fork,reuseaddr", "EXEC:'python3 /app/slightslant.py'" ]
