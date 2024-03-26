from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
import logging
from flask import Flask, jsonify
from kafka import KafkaConsumer

app = Flask(__name__)

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'kafka-service:9092'

db = SQLAlchemy()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-api-location-service-start")

def consume_messages():
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
    for message in consumer:
        # Process the message as needed
        logger.info(message.value.decode('utf-8'))
        print(message.value.decode('utf-8'))  # For example, print the message to console


def create_app(env=None):
    import threading
    from app.config import config_by_name
    from app.routes import register_routes

    kafka_thread = threading.Thread(target=consume_messages)
    kafka_thread.daemon = True
    kafka_thread.start()

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
