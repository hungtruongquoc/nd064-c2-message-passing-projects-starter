FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY api/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

# Copy the api directory into /app
COPY api ./api
COPY __init__.py .

# Copy the shared directory into /app
COPY shared ./shared

ENV FLASK_APP=./api/wsgi.py
ENV PYTHONPATH=/app
CMD ["flask", "run", "--host", "0.0.0.0"]