FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY modules/api/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

# Copy the service directory into /app/person_service
COPY modules/api ./modules/api

# Copy the shared directory into /app/shared
COPY modules/shared ./modules/shared

ENV FLASK_APP=modules/api/wsgi.py
CMD ["flask", "run", "--host", "0.0.0.0"]