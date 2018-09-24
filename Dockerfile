FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh