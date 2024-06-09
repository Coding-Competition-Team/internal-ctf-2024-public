FROM node:22-bullseye

RUN apt update && \
    apt install -y socat

RUN useradd prisoner

COPY . .

RUN chmod 644 /flag.txt
RUN chmod 744 /main.js 

USER prisoner

EXPOSE 7021

CMD [ "socat", "tcp-listen:7021,fork,reuseaddr", "EXEC:'node main.js'" ]
