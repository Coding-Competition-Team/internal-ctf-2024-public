FROM python:3.11-slim-bookworm

COPY ./build/ .

RUN python3 -m pip install flask

EXPOSE 7011

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["flask", "run", "--host=0.0.0.0", "--port=7011", "--no-reload"] 