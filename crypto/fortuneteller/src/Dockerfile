FROM python:3.10

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir pwn && \
    pip3 install --no-cache-dir randcrack && \
    pip install --no-cache-dir pycryptodome

RUN apt update && \
    apt install -y socat

WORKDIR /app
COPY . .

CMD [ "socat", "tcp-listen:4001,fork,reuseaddr", "EXEC:'python3 /app/run.py'" ]
