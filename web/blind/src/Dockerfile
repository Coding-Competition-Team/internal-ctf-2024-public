FROM python:3.11-slim-bookworm

COPY app.py app.py

RUN python3 -m pip install flask

EXPOSE 7013

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["flask", "run", "--host=0.0.0.0", "--port=7013", "--no-reload"] 