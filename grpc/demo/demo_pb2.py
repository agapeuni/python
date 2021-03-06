# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='demo.code',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndemo.proto\x12\tdemo.code\"*\n\x0b\x44\x65moRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"+\n\x0c\x44\x65moResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05total\x18\x02 \x01(\x05\x32\xfa\x01\n\x04\x44\x65mo\x12;\n\x06Select\x12\x16.demo.code.DemoRequest\x1a\x17.demo.code.DemoResponse\"\x00\x12;\n\x06Insert\x12\x16.demo.code.DemoRequest\x1a\x17.demo.code.DemoResponse\"\x00\x12;\n\x06Update\x12\x16.demo.code.DemoRequest\x1a\x17.demo.code.DemoResponse\"\x00\x12;\n\x06\x44\x65lete\x12\x16.demo.code.DemoRequest\x1a\x17.demo.code.DemoResponse\"\x00\x62\x06proto3'
)




_DEMOREQUEST = _descriptor.Descriptor(
  name='DemoRequest',
  full_name='demo.code.DemoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='demo.code.DemoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='demo.code.DemoRequest.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=67,
)


_DEMORESPONSE = _descriptor.Descriptor(
  name='DemoResponse',
  full_name='demo.code.DemoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='demo.code.DemoResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='demo.code.DemoResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['DemoRequest'] = _DEMOREQUEST
DESCRIPTOR.message_types_by_name['DemoResponse'] = _DEMORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DemoRequest = _reflection.GeneratedProtocolMessageType('DemoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEMOREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.code.DemoRequest)
  })
_sym_db.RegisterMessage(DemoRequest)

DemoResponse = _reflection.GeneratedProtocolMessageType('DemoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEMORESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.code.DemoResponse)
  })
_sym_db.RegisterMessage(DemoResponse)



_DEMO = _descriptor.ServiceDescriptor(
  name='Demo',
  full_name='demo.code.Demo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=115,
  serialized_end=365,
  methods=[
  _descriptor.MethodDescriptor(
    name='Select',
    full_name='demo.code.Demo.Select',
    index=0,
    containing_service=None,
    input_type=_DEMOREQUEST,
    output_type=_DEMORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='demo.code.Demo.Insert',
    index=1,
    containing_service=None,
    input_type=_DEMOREQUEST,
    output_type=_DEMORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='demo.code.Demo.Update',
    index=2,
    containing_service=None,
    input_type=_DEMOREQUEST,
    output_type=_DEMORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='demo.code.Demo.Delete',
    index=3,
    containing_service=None,
    input_type=_DEMOREQUEST,
    output_type=_DEMORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEMO)

DESCRIPTOR.services_by_name['Demo'] = _DEMO

# @@protoc_insertion_point(module_scope)
