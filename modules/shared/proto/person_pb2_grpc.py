# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import person_pb2 as person__pb2


class PersonServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/PersonService/Create',
                request_serializer=person__pb2.Person.SerializeToString,
                response_deserializer=person__pb2.Person.FromString,
                )
        self.GetPerson = channel.unary_unary(
                '/PersonService/GetPerson',
                request_serializer=person__pb2.PersonId.SerializeToString,
                response_deserializer=person__pb2.Person.FromString,
                )
        self.GetPersonList = channel.unary_unary(
                '/PersonService/GetPersonList',
                request_serializer=person__pb2.PersonIdList.SerializeToString,
                response_deserializer=person__pb2.PersonList.FromString,
                )


class PersonServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPersonList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=person__pb2.Person.FromString,
                    response_serializer=person__pb2.Person.SerializeToString,
            ),
            'GetPerson': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPerson,
                    request_deserializer=person__pb2.PersonId.FromString,
                    response_serializer=person__pb2.Person.SerializeToString,
            ),
            'GetPersonList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonList,
                    request_deserializer=person__pb2.PersonIdList.FromString,
                    response_serializer=person__pb2.PersonList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PersonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/Create',
            person__pb2.Person.SerializeToString,
            person__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/GetPerson',
            person__pb2.PersonId.SerializeToString,
            person__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPersonList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/GetPersonList',
            person__pb2.PersonIdList.SerializeToString,
            person__pb2.PersonList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
