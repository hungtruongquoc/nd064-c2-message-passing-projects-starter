import logging

from ..database import db
from .models import Person
from modules.shared.proto import person_pb2
from modules.shared.proto import person_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-api-person-service")


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def Create(self, request, context):
        new_person = Person()
        new_person.first_name = request.first_name
        new_person.last_name = request.last_name
        new_person.company_name = request.company_name

        db.session.add(new_person)
        db.session.commit()

        return person_pb2.Person(id=new_person.id, first_name=new_person.first_name, last_name=new_person.last_name,
                                 company_name=new_person.company_name)

    def GetPerson(self, request, context):
        person = db.session.query(Person).get(request.id)
        return person_pb2.Person(id=person.id, first_name=person.first_name, last_name=person.last_name,
                                 company_name=person.company_name)

    def GetPersonList(self, request, context):
        logger.info("Received request to get all persons from a gRPC call")
        # Query the database for persons with ids in the list
        persons = db.session.query(Person).all()

        # Create a PersonList message
        person_list = person_pb2.PersonList()

        logger.info("Retrieved all persons from the database")

        # For each person, create a Person protobuf message and add it to the PersonList message
        for person in persons:
            person_message = person_pb2.Person(
                id=person.id,
                first_name=person.first_name,
                last_name=person.last_name,
                company_name=person.company_name
            )
            person_list.persons.append(person_message)

        logger.info("Sending PersonList message")

        # Return the PersonList message
        return person_list
