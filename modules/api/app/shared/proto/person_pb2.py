# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cperson.proto\"Q\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"\x1b\n\x0cPersonIdList\x12\x0b\n\x03ids\x18\x01 \x03(\x05\"\x16\n\x08PersonId\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\nPersonList\x12\x17\n\x06people\x18\x01 \x03(\x0b\x32\x07.Person2y\n\rPersonService\x12\x1a\n\x06\x43reate\x12\x07.Person\x1a\x07.Person\x12\x1f\n\tGetPerson\x12\t.PersonId\x1a\x07.Person\x12+\n\rGetPersonList\x12\r.PersonIdList\x1a\x0b.PersonListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'person_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PERSON']._serialized_start=16
  _globals['_PERSON']._serialized_end=97
  _globals['_PERSONIDLIST']._serialized_start=99
  _globals['_PERSONIDLIST']._serialized_end=126
  _globals['_PERSONID']._serialized_start=128
  _globals['_PERSONID']._serialized_end=150
  _globals['_PERSONLIST']._serialized_start=152
  _globals['_PERSONLIST']._serialized_end=189
  _globals['_PERSONSERVICE']._serialized_start=191
  _globals['_PERSONSERVICE']._serialized_end=312
# @@protoc_insertion_point(module_scope)
