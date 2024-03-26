from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
import logging
import json
from flask import Flask, jsonify
from kafka import KafkaConsumer

app = Flask(__name__)

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'kafka-service:9092'

db = SQLAlchemy()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-api-location-service-start")


def consume_messages(app: Flask):
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
    for message in consumer:
        logger.info("Received message: %s", message.value.decode('utf-8'))
        # Process the message as needed
        data: dict = json.loads(message.value.decode('utf-8'))
        logger.info(data.get('person_id'))

        # Create a Flask test client
        test_client = app.test_client()

        # Construct a POST request to /locations endpoint
        response = test_client.post('/api/locations', json=data)

        logger.info("Result: %s", response)


def create_app(env=None):
    import threading
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    # Starts the Kafka consumer thread
    kafka_thread = threading.Thread(target=consume_messages, args=(app,))
    kafka_thread.daemon = True
    kafka_thread.start()

    return app
