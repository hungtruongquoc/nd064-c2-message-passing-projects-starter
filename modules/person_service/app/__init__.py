from concurrent import futures
import logging

import grpc
from flask import Flask
from .database import db

from .udaconnect.services import PersonServicer
from modules.shared.proto import person_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-api-person-service")

def create_app(env=None):
    from .config import config_by_name

    app = Flask(__name__)

    app.config.from_object(config_by_name[env or "test"])

    db.init_app(app)
    # Initialize gRPC server
    logger.info("Initializing server instance ...")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(app), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    logger.info("gRPC server started on port 5000 ...")
    server.wait_for_termination()
#
# if __name__ == "__main__":
#     create_app()
