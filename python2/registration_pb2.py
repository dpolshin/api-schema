# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='registration.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=_b('\342?\026\n\024im.dlg.grpc.services'),
  serialized_pb=_b('\n\x12registration.proto\x12\x06\x64ialog\x1a\x15scalapb/scalapb.proto\x1a\x1cgoogle/api/annotations.proto\"\x81\x01\n\x15RequestRegisterDevice\x12\x11\n\tclient_pk\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\x05\x12\x11\n\tapp_title\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x65vice_title\x18\x04 \x01(\t:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"i\n\x15ResponseDeviceRequest\x12\x11\n\tserver_pk\x18\x01 \x01(\x0c\x12\x0f\n\x07\x61uth_id\x18\x02 \x01(\x03\x12\r\n\x05token\x18\x03 \x01(\t:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"!\n\x1fRegisterDeprecatedDeviceRequest\"C\n\x1dRequestExchangeAuthIdForToken\x12\x0f\n\x07\x61uth_id\x18\x01 \x01(\x03\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x32\xc9\x03\n\x0cRegistration\x12\x97\x01\n\x16\x45xchangeAuthIdForToken\x12%.dialog.RequestExchangeAuthIdForToken\x1a\x1d.dialog.ResponseDeviceRequest\"7\x82\xd3\xe4\x93\x02\x31\",/v1/grpc/Registration/ExchangeAuthIdForToken:\x01*\x12\x7f\n\x0eRegisterDevice\x12\x1d.dialog.RequestRegisterDevice\x1a\x1d.dialog.ResponseDeviceRequest\"/\x82\xd3\xe4\x93\x02)\"$/v1/grpc/Registration/RegisterDevice:\x01*\x12\x9d\x01\n\x18RegisterDeprecatedDevice\x12\'.dialog.RegisterDeprecatedDeviceRequest\x1a\x1d.dialog.ResponseDeviceRequest\"9\x82\xd3\xe4\x93\x02\x33\"./v1/grpc/Registration/RegisterDeprecatedDevice:\x01*B\x19\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3')
  ,
  dependencies=[scalapb_dot_scalapb__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_REQUESTREGISTERDEVICE = _descriptor.Descriptor(
  name='RequestRegisterDevice',
  full_name='dialog.RequestRegisterDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_pk', full_name='dialog.RequestRegisterDevice.client_pk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='dialog.RequestRegisterDevice.app_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_title', full_name='dialog.RequestRegisterDevice.app_title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_title', full_name='dialog.RequestRegisterDevice.device_title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\031\n\027im.dlg.grpc.GrpcRequest'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=213,
)


_RESPONSEDEVICEREQUEST = _descriptor.Descriptor(
  name='ResponseDeviceRequest',
  full_name='dialog.ResponseDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_pk', full_name='dialog.ResponseDeviceRequest.server_pk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_id', full_name='dialog.ResponseDeviceRequest.auth_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='dialog.ResponseDeviceRequest.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\032\n\030im.dlg.grpc.GrpcResponse'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=320,
)


_REGISTERDEPRECATEDDEVICEREQUEST = _descriptor.Descriptor(
  name='RegisterDeprecatedDeviceRequest',
  full_name='dialog.RegisterDeprecatedDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=322,
  serialized_end=355,
)


_REQUESTEXCHANGEAUTHIDFORTOKEN = _descriptor.Descriptor(
  name='RequestExchangeAuthIdForToken',
  full_name='dialog.RequestExchangeAuthIdForToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_id', full_name='dialog.RequestExchangeAuthIdForToken.auth_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='dialog.RequestExchangeAuthIdForToken.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=357,
  serialized_end=424,
)

DESCRIPTOR.message_types_by_name['RequestRegisterDevice'] = _REQUESTREGISTERDEVICE
DESCRIPTOR.message_types_by_name['ResponseDeviceRequest'] = _RESPONSEDEVICEREQUEST
DESCRIPTOR.message_types_by_name['RegisterDeprecatedDeviceRequest'] = _REGISTERDEPRECATEDDEVICEREQUEST
DESCRIPTOR.message_types_by_name['RequestExchangeAuthIdForToken'] = _REQUESTEXCHANGEAUTHIDFORTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestRegisterDevice = _reflection.GeneratedProtocolMessageType('RequestRegisterDevice', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTREGISTERDEVICE,
  __module__ = 'registration_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRegisterDevice)
  ))
_sym_db.RegisterMessage(RequestRegisterDevice)

ResponseDeviceRequest = _reflection.GeneratedProtocolMessageType('ResponseDeviceRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEDEVICEREQUEST,
  __module__ = 'registration_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseDeviceRequest)
  ))
_sym_db.RegisterMessage(ResponseDeviceRequest)

RegisterDeprecatedDeviceRequest = _reflection.GeneratedProtocolMessageType('RegisterDeprecatedDeviceRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERDEPRECATEDDEVICEREQUEST,
  __module__ = 'registration_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RegisterDeprecatedDeviceRequest)
  ))
_sym_db.RegisterMessage(RegisterDeprecatedDeviceRequest)

RequestExchangeAuthIdForToken = _reflection.GeneratedProtocolMessageType('RequestExchangeAuthIdForToken', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTEXCHANGEAUTHIDFORTOKEN,
  __module__ = 'registration_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestExchangeAuthIdForToken)
  ))
_sym_db.RegisterMessage(RequestExchangeAuthIdForToken)


DESCRIPTOR._options = None
_REQUESTREGISTERDEVICE._options = None
_RESPONSEDEVICEREQUEST._options = None

_REGISTRATION = _descriptor.ServiceDescriptor(
  name='Registration',
  full_name='dialog.Registration',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=427,
  serialized_end=884,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExchangeAuthIdForToken',
    full_name='dialog.Registration.ExchangeAuthIdForToken',
    index=0,
    containing_service=None,
    input_type=_REQUESTEXCHANGEAUTHIDFORTOKEN,
    output_type=_RESPONSEDEVICEREQUEST,
    serialized_options=_b('\202\323\344\223\0021\",/v1/grpc/Registration/ExchangeAuthIdForToken:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RegisterDevice',
    full_name='dialog.Registration.RegisterDevice',
    index=1,
    containing_service=None,
    input_type=_REQUESTREGISTERDEVICE,
    output_type=_RESPONSEDEVICEREQUEST,
    serialized_options=_b('\202\323\344\223\002)\"$/v1/grpc/Registration/RegisterDevice:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RegisterDeprecatedDevice',
    full_name='dialog.Registration.RegisterDeprecatedDevice',
    index=2,
    containing_service=None,
    input_type=_REGISTERDEPRECATEDDEVICEREQUEST,
    output_type=_RESPONSEDEVICEREQUEST,
    serialized_options=_b('\202\323\344\223\0023\"./v1/grpc/Registration/RegisterDeprecatedDevice:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTRATION)

DESCRIPTOR.services_by_name['Registration'] = _REGISTRATION

# @@protoc_insertion_point(module_scope)