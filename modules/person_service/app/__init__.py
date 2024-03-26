from concurrent import futures

import grpc
from flask import Flask
from .database import db

from .udaconnect.services import PersonServicer
from modules.shared.proto import person_pb2_grpc


def create_app(env=None):
    from .config import config_by_name

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])

    db.init_app(app)
    # Initialize gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)

    server.start()
    # server.add_insecure_port("[::]:5000")
    server.add_insecure_port("0.0.0.0:5000")
    server.wait_for_termination()

    return app

#
# if __name__ == "__main__":
#     create_app()
