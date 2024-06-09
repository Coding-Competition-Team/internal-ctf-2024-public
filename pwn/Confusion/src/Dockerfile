FROM pwn.red/jail

COPY --from=ubuntu:22.04@sha256:f9d633ff6640178c2d0525017174a688e2c1aef28f0a0130b26bd5554491f0da / /srv

COPY ./flag.txt /srv/app/flag.txt
ADD ./confusion /srv/app/run  

EXPOSE 5000

RUN chmod 444 /srv/app/flag.txt
RUN chmod +x /srv/app/run
