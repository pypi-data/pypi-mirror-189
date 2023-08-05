# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/fleet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import task_pb2 as flwr_dot_proto_dot_task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flwr/proto/fleet.proto',
  package='flwr.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x66lwr/proto/fleet.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x15\x66lwr/proto/task.proto\"F\n\x12PullTaskInsRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"k\n\x13PullTaskInsResponse\x12(\n\treconnect\x18\x01 \x01(\x0b\x32\x15.flwr.proto.Reconnect\x12*\n\rtask_ins_list\x18\x02 \x03(\x0b\x32\x13.flwr.proto.TaskIns\"@\n\x12PushTaskResRequest\x12*\n\rtask_res_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskRes\"\xae\x01\n\x13PushTaskResResponse\x12(\n\treconnect\x18\x01 \x01(\x0b\x32\x15.flwr.proto.Reconnect\x12=\n\x07results\x18\x02 \x03(\x0b\x32,.flwr.proto.PushTaskResResponse.ResultsEntry\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\x1e\n\tReconnect\x12\x11\n\treconnect\x18\x01 \x01(\x04\x32\xab\x01\n\x05\x46leet\x12P\n\x0bPullTaskIns\x12\x1e.flwr.proto.PullTaskInsRequest\x1a\x1f.flwr.proto.PullTaskInsResponse\"\x00\x12P\n\x0bPushTaskRes\x12\x1e.flwr.proto.PushTaskResRequest\x1a\x1f.flwr.proto.PushTaskResResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[flwr_dot_proto_dot_node__pb2.DESCRIPTOR,flwr_dot_proto_dot_task__pb2.DESCRIPTOR,])




_PULLTASKINSREQUEST = _descriptor.Descriptor(
  name='PullTaskInsRequest',
  full_name='flwr.proto.PullTaskInsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='flwr.proto.PullTaskInsRequest.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_ids', full_name='flwr.proto.PullTaskInsRequest.task_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=84,
  serialized_end=154,
)


_PULLTASKINSRESPONSE = _descriptor.Descriptor(
  name='PullTaskInsResponse',
  full_name='flwr.proto.PullTaskInsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reconnect', full_name='flwr.proto.PullTaskInsResponse.reconnect', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_ins_list', full_name='flwr.proto.PullTaskInsResponse.task_ins_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=156,
  serialized_end=263,
)


_PUSHTASKRESREQUEST = _descriptor.Descriptor(
  name='PushTaskResRequest',
  full_name='flwr.proto.PushTaskResRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_res_list', full_name='flwr.proto.PushTaskResRequest.task_res_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=265,
  serialized_end=329,
)


_PUSHTASKRESRESPONSE_RESULTSENTRY = _descriptor.Descriptor(
  name='ResultsEntry',
  full_name='flwr.proto.PushTaskResResponse.ResultsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flwr.proto.PushTaskResResponse.ResultsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='flwr.proto.PushTaskResResponse.ResultsEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=506,
)

_PUSHTASKRESRESPONSE = _descriptor.Descriptor(
  name='PushTaskResResponse',
  full_name='flwr.proto.PushTaskResResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reconnect', full_name='flwr.proto.PushTaskResResponse.reconnect', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='flwr.proto.PushTaskResResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PUSHTASKRESRESPONSE_RESULTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=332,
  serialized_end=506,
)


_RECONNECT = _descriptor.Descriptor(
  name='Reconnect',
  full_name='flwr.proto.Reconnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reconnect', full_name='flwr.proto.Reconnect.reconnect', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=508,
  serialized_end=538,
)

_PULLTASKINSREQUEST.fields_by_name['node'].message_type = flwr_dot_proto_dot_node__pb2._NODE
_PULLTASKINSRESPONSE.fields_by_name['reconnect'].message_type = _RECONNECT
_PULLTASKINSRESPONSE.fields_by_name['task_ins_list'].message_type = flwr_dot_proto_dot_task__pb2._TASKINS
_PUSHTASKRESREQUEST.fields_by_name['task_res_list'].message_type = flwr_dot_proto_dot_task__pb2._TASKRES
_PUSHTASKRESRESPONSE_RESULTSENTRY.containing_type = _PUSHTASKRESRESPONSE
_PUSHTASKRESRESPONSE.fields_by_name['reconnect'].message_type = _RECONNECT
_PUSHTASKRESRESPONSE.fields_by_name['results'].message_type = _PUSHTASKRESRESPONSE_RESULTSENTRY
DESCRIPTOR.message_types_by_name['PullTaskInsRequest'] = _PULLTASKINSREQUEST
DESCRIPTOR.message_types_by_name['PullTaskInsResponse'] = _PULLTASKINSRESPONSE
DESCRIPTOR.message_types_by_name['PushTaskResRequest'] = _PUSHTASKRESREQUEST
DESCRIPTOR.message_types_by_name['PushTaskResResponse'] = _PUSHTASKRESRESPONSE
DESCRIPTOR.message_types_by_name['Reconnect'] = _RECONNECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PullTaskInsRequest = _reflection.GeneratedProtocolMessageType('PullTaskInsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PULLTASKINSREQUEST,
  '__module__' : 'flwr.proto.fleet_pb2'
  # @@protoc_insertion_point(class_scope:flwr.proto.PullTaskInsRequest)
  })
_sym_db.RegisterMessage(PullTaskInsRequest)

PullTaskInsResponse = _reflection.GeneratedProtocolMessageType('PullTaskInsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PULLTASKINSRESPONSE,
  '__module__' : 'flwr.proto.fleet_pb2'
  # @@protoc_insertion_point(class_scope:flwr.proto.PullTaskInsResponse)
  })
_sym_db.RegisterMessage(PullTaskInsResponse)

PushTaskResRequest = _reflection.GeneratedProtocolMessageType('PushTaskResRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUSHTASKRESREQUEST,
  '__module__' : 'flwr.proto.fleet_pb2'
  # @@protoc_insertion_point(class_scope:flwr.proto.PushTaskResRequest)
  })
_sym_db.RegisterMessage(PushTaskResRequest)

PushTaskResResponse = _reflection.GeneratedProtocolMessageType('PushTaskResResponse', (_message.Message,), {

  'ResultsEntry' : _reflection.GeneratedProtocolMessageType('ResultsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUSHTASKRESRESPONSE_RESULTSENTRY,
    '__module__' : 'flwr.proto.fleet_pb2'
    # @@protoc_insertion_point(class_scope:flwr.proto.PushTaskResResponse.ResultsEntry)
    })
  ,
  'DESCRIPTOR' : _PUSHTASKRESRESPONSE,
  '__module__' : 'flwr.proto.fleet_pb2'
  # @@protoc_insertion_point(class_scope:flwr.proto.PushTaskResResponse)
  })
_sym_db.RegisterMessage(PushTaskResResponse)
_sym_db.RegisterMessage(PushTaskResResponse.ResultsEntry)

Reconnect = _reflection.GeneratedProtocolMessageType('Reconnect', (_message.Message,), {
  'DESCRIPTOR' : _RECONNECT,
  '__module__' : 'flwr.proto.fleet_pb2'
  # @@protoc_insertion_point(class_scope:flwr.proto.Reconnect)
  })
_sym_db.RegisterMessage(Reconnect)


_PUSHTASKRESRESPONSE_RESULTSENTRY._options = None

_FLEET = _descriptor.ServiceDescriptor(
  name='Fleet',
  full_name='flwr.proto.Fleet',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=541,
  serialized_end=712,
  methods=[
  _descriptor.MethodDescriptor(
    name='PullTaskIns',
    full_name='flwr.proto.Fleet.PullTaskIns',
    index=0,
    containing_service=None,
    input_type=_PULLTASKINSREQUEST,
    output_type=_PULLTASKINSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PushTaskRes',
    full_name='flwr.proto.Fleet.PushTaskRes',
    index=1,
    containing_service=None,
    input_type=_PUSHTASKRESREQUEST,
    output_type=_PUSHTASKRESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLEET)

DESCRIPTOR.services_by_name['Fleet'] = _FLEET

# @@protoc_insertion_point(module_scope)
