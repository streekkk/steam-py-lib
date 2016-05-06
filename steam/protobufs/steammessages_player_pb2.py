# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_player.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import steammessages_unified_base_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_player.proto',
  package='',
  serialized_pb='\n\x1asteammessages_player.proto\x1a steammessages_unified_base.proto\"3\n\"CPlayer_GetGameBadgeLevels_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\xb5\x01\n#CPlayer_GetGameBadgeLevels_Response\x12\x14\n\x0cplayer_level\x18\x01 \x01(\r\x12:\n\x06\x62\x61\x64ges\x18\x02 \x03(\x0b\x32*.CPlayer_GetGameBadgeLevels_Response.Badge\x1a<\n\x05\x42\x61\x64ge\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x0e\n\x06series\x18\x02 \x01(\x05\x12\x14\n\x0c\x62order_color\x18\x03 \x01(\r\"\x82\x01\n\"CPlayer_GetLastPlayedTimes_Request\x12\\\n\x0fmin_last_played\x18\x01 \x01(\rBC\x82\xb5\x18?The most recent last-played time the client already knows about\"\xc0\x01\n#CPlayer_GetLastPlayedTimes_Response\x12\x38\n\x05games\x18\x01 \x03(\x0b\x32).CPlayer_GetLastPlayedTimes_Response.Game\x1a_\n\x04Game\x12\r\n\x05\x61ppid\x18\x01 \x01(\x05\x12\x15\n\rlast_playtime\x18\x02 \x01(\r\x12\x17\n\x0fplaytime_2weeks\x18\x03 \x01(\x05\x12\x18\n\x10playtime_forever\x18\x04 \x01(\x05\"\x1b\n\x19\x43Player_AcceptSSA_Request\"\x1c\n\x1a\x43Player_AcceptSSA_Response\"`\n$CPlayer_LastPlayedTimes_Notification\x12\x38\n\x05games\x18\x01 \x03(\x0b\x32).CPlayer_GetLastPlayedTimes_Response.Game\",\n*CPlayerClient_GetSystemInformation_Request\"\xf5\x04\n\x11\x43\x43lientSystemInfo\x12#\n\x03\x63pu\x18\x01 \x01(\x0b\x32\x16.CClientSystemInfo.CPU\x12\x30\n\nvideo_card\x18\x02 \x01(\x0b\x32\x1c.CClientSystemInfo.VideoCard\x12\x18\n\x10operating_system\x18\x03 \x01(\t\x12\x10\n\x08os_64bit\x18\x04 \x01(\x08\x12\x15\n\rsystem_ram_mb\x18\x05 \x01(\x05\x12\x14\n\x0c\x61udio_device\x18\x06 \x01(\t\x12\x1c\n\x14\x61udio_driver_version\x18\x07 \x01(\t\x1a\xe0\x01\n\x03\x43PU\x12\x11\n\tspeed_mhz\x18\x01 \x01(\x05\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x12\x1a\n\x12logical_processors\x18\x03 \x01(\x05\x12\x1b\n\x13physical_processors\x18\x04 \x01(\x05\x12\x16\n\x0ehyperthreading\x18\x05 \x01(\x08\x12\r\n\x05\x66\x63mov\x18\x06 \x01(\x08\x12\x0c\n\x04sse2\x18\x07 \x01(\x08\x12\x0c\n\x04sse3\x18\x08 \x01(\x08\x12\r\n\x05ssse3\x18\t \x01(\x08\x12\r\n\x05sse4a\x18\n \x01(\x08\x12\r\n\x05sse41\x18\x0b \x01(\x08\x12\r\n\x05sse42\x18\x0c \x01(\x08\x1a\xae\x01\n\tVideoCard\x12\x0e\n\x06\x64river\x18\x01 \x01(\t\x12\x16\n\x0e\x64river_version\x18\x02 \x01(\t\x12\x13\n\x0b\x64river_date\x18\x03 \x01(\r\x12\x17\n\x0f\x64irectx_version\x18\x04 \x01(\t\x12\x16\n\x0eopengl_version\x18\x05 \x01(\t\x12\x10\n\x08vendorid\x18\x06 \x01(\x05\x12\x10\n\x08\x64\x65viceid\x18\x07 \x01(\x05\x12\x0f\n\x07vram_mb\x18\x08 \x01(\x05\"V\n+CPlayerClient_GetSystemInformation_Response\x12\'\n\x0bsystem_info\x18\x01 \x01(\x0b\x32\x12.CClientSystemInfo2\xed\x03\n\x06Player\x12\xb6\x01\n\x12GetGameBadgeLevels\x12#.CPlayer_GetGameBadgeLevels_Request\x1a$.CPlayer_GetGameBadgeLevels_Response\"U\x82\xb5\x18QReturns the Steam Level of a user, the Badge level for the game, and if it\'s foil\x12\x95\x01\n\x18\x43lientGetLastPlayedTimes\x12#.CPlayer_GetLastPlayedTimes_Request\x1a$.CPlayer_GetLastPlayedTimes_Response\".\x82\xb5\x18*Gets the last-played times for the account\x12\x63\n\tAcceptSSA\x12\x1a.CPlayer_AcceptSSA_Request\x1a\x1b.CPlayer_AcceptSSA_Response\"\x1d\x82\xb5\x18\x19User is accepting the SSA\x1a-\x82\xb5\x18)A service for accessing Steam player data2\x93\x03\n\x0cPlayerClient\x12\x8c\x01\n\x15NotifyLastPlayedTimes\x12%.CPlayer_LastPlayedTimes_Notification\x1a\x0b.NoResponse\"?\x82\xb5\x18;Notification from server to client of more recent play time\x12\xc3\x01\n\x14GetSystemInformation\x12+.CPlayerClient_GetSystemInformation_Request\x1a,.CPlayerClient_GetSystemInformation_Response\"P\x82\xb5\x18LRequest from the server to the client for information about the users system\x1a.\x82\xb5\x18&Steam player data client notifications\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')




_CPLAYER_GETGAMEBADGELEVELS_REQUEST = _descriptor.Descriptor(
  name='CPlayer_GetGameBadgeLevels_Request',
  full_name='CPlayer_GetGameBadgeLevels_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CPlayer_GetGameBadgeLevels_Request.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=64,
  serialized_end=115,
)


_CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE = _descriptor.Descriptor(
  name='Badge',
  full_name='CPlayer_GetGameBadgeLevels_Response.Badge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='CPlayer_GetGameBadgeLevels_Response.Badge.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='series', full_name='CPlayer_GetGameBadgeLevels_Response.Badge.series', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_color', full_name='CPlayer_GetGameBadgeLevels_Response.Badge.border_color', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=239,
  serialized_end=299,
)

_CPLAYER_GETGAMEBADGELEVELS_RESPONSE = _descriptor.Descriptor(
  name='CPlayer_GetGameBadgeLevels_Response',
  full_name='CPlayer_GetGameBadgeLevels_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_level', full_name='CPlayer_GetGameBadgeLevels_Response.player_level', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='badges', full_name='CPlayer_GetGameBadgeLevels_Response.badges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=118,
  serialized_end=299,
)


_CPLAYER_GETLASTPLAYEDTIMES_REQUEST = _descriptor.Descriptor(
  name='CPlayer_GetLastPlayedTimes_Request',
  full_name='CPlayer_GetLastPlayedTimes_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_last_played', full_name='CPlayer_GetLastPlayedTimes_Request.min_last_played', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030?The most recent last-played time the client already knows about')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=302,
  serialized_end=432,
)


_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME = _descriptor.Descriptor(
  name='Game',
  full_name='CPlayer_GetLastPlayedTimes_Response.Game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CPlayer_GetLastPlayedTimes_Response.Game.appid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_playtime', full_name='CPlayer_GetLastPlayedTimes_Response.Game.last_playtime', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playtime_2weeks', full_name='CPlayer_GetLastPlayedTimes_Response.Game.playtime_2weeks', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playtime_forever', full_name='CPlayer_GetLastPlayedTimes_Response.Game.playtime_forever', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=532,
  serialized_end=627,
)

_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE = _descriptor.Descriptor(
  name='CPlayer_GetLastPlayedTimes_Response',
  full_name='CPlayer_GetLastPlayedTimes_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='games', full_name='CPlayer_GetLastPlayedTimes_Response.games', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=435,
  serialized_end=627,
)


_CPLAYER_ACCEPTSSA_REQUEST = _descriptor.Descriptor(
  name='CPlayer_AcceptSSA_Request',
  full_name='CPlayer_AcceptSSA_Request',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=629,
  serialized_end=656,
)


_CPLAYER_ACCEPTSSA_RESPONSE = _descriptor.Descriptor(
  name='CPlayer_AcceptSSA_Response',
  full_name='CPlayer_AcceptSSA_Response',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=658,
  serialized_end=686,
)


_CPLAYER_LASTPLAYEDTIMES_NOTIFICATION = _descriptor.Descriptor(
  name='CPlayer_LastPlayedTimes_Notification',
  full_name='CPlayer_LastPlayedTimes_Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='games', full_name='CPlayer_LastPlayedTimes_Notification.games', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=688,
  serialized_end=784,
)


_CPLAYERCLIENT_GETSYSTEMINFORMATION_REQUEST = _descriptor.Descriptor(
  name='CPlayerClient_GetSystemInformation_Request',
  full_name='CPlayerClient_GetSystemInformation_Request',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=786,
  serialized_end=830,
)


_CCLIENTSYSTEMINFO_CPU = _descriptor.Descriptor(
  name='CPU',
  full_name='CClientSystemInfo.CPU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed_mhz', full_name='CClientSystemInfo.CPU.speed_mhz', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='CClientSystemInfo.CPU.vendor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logical_processors', full_name='CClientSystemInfo.CPU.logical_processors', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physical_processors', full_name='CClientSystemInfo.CPU.physical_processors', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hyperthreading', full_name='CClientSystemInfo.CPU.hyperthreading', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fcmov', full_name='CClientSystemInfo.CPU.fcmov', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sse2', full_name='CClientSystemInfo.CPU.sse2', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sse3', full_name='CClientSystemInfo.CPU.sse3', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssse3', full_name='CClientSystemInfo.CPU.ssse3', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sse4a', full_name='CClientSystemInfo.CPU.sse4a', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sse41', full_name='CClientSystemInfo.CPU.sse41', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sse42', full_name='CClientSystemInfo.CPU.sse42', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1061,
  serialized_end=1285,
)

_CCLIENTSYSTEMINFO_VIDEOCARD = _descriptor.Descriptor(
  name='VideoCard',
  full_name='CClientSystemInfo.VideoCard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver', full_name='CClientSystemInfo.VideoCard.driver', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driver_version', full_name='CClientSystemInfo.VideoCard.driver_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driver_date', full_name='CClientSystemInfo.VideoCard.driver_date', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='directx_version', full_name='CClientSystemInfo.VideoCard.directx_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opengl_version', full_name='CClientSystemInfo.VideoCard.opengl_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vendorid', full_name='CClientSystemInfo.VideoCard.vendorid', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceid', full_name='CClientSystemInfo.VideoCard.deviceid', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vram_mb', full_name='CClientSystemInfo.VideoCard.vram_mb', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1288,
  serialized_end=1462,
)

_CCLIENTSYSTEMINFO = _descriptor.Descriptor(
  name='CClientSystemInfo',
  full_name='CClientSystemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='CClientSystemInfo.cpu', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_card', full_name='CClientSystemInfo.video_card', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operating_system', full_name='CClientSystemInfo.operating_system', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='os_64bit', full_name='CClientSystemInfo.os_64bit', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_ram_mb', full_name='CClientSystemInfo.system_ram_mb', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_device', full_name='CClientSystemInfo.audio_device', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_driver_version', full_name='CClientSystemInfo.audio_driver_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CCLIENTSYSTEMINFO_CPU, _CCLIENTSYSTEMINFO_VIDEOCARD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=833,
  serialized_end=1462,
)


_CPLAYERCLIENT_GETSYSTEMINFORMATION_RESPONSE = _descriptor.Descriptor(
  name='CPlayerClient_GetSystemInformation_Response',
  full_name='CPlayerClient_GetSystemInformation_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system_info', full_name='CPlayerClient_GetSystemInformation_Response.system_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1464,
  serialized_end=1550,
)

_CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE.containing_type = _CPLAYER_GETGAMEBADGELEVELS_RESPONSE;
_CPLAYER_GETGAMEBADGELEVELS_RESPONSE.fields_by_name['badges'].message_type = _CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE
_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME.containing_type = _CPLAYER_GETLASTPLAYEDTIMES_RESPONSE;
_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE.fields_by_name['games'].message_type = _CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME
_CPLAYER_LASTPLAYEDTIMES_NOTIFICATION.fields_by_name['games'].message_type = _CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME
_CCLIENTSYSTEMINFO_CPU.containing_type = _CCLIENTSYSTEMINFO;
_CCLIENTSYSTEMINFO_VIDEOCARD.containing_type = _CCLIENTSYSTEMINFO;
_CCLIENTSYSTEMINFO.fields_by_name['cpu'].message_type = _CCLIENTSYSTEMINFO_CPU
_CCLIENTSYSTEMINFO.fields_by_name['video_card'].message_type = _CCLIENTSYSTEMINFO_VIDEOCARD
_CPLAYERCLIENT_GETSYSTEMINFORMATION_RESPONSE.fields_by_name['system_info'].message_type = _CCLIENTSYSTEMINFO
DESCRIPTOR.message_types_by_name['CPlayer_GetGameBadgeLevels_Request'] = _CPLAYER_GETGAMEBADGELEVELS_REQUEST
DESCRIPTOR.message_types_by_name['CPlayer_GetGameBadgeLevels_Response'] = _CPLAYER_GETGAMEBADGELEVELS_RESPONSE
DESCRIPTOR.message_types_by_name['CPlayer_GetLastPlayedTimes_Request'] = _CPLAYER_GETLASTPLAYEDTIMES_REQUEST
DESCRIPTOR.message_types_by_name['CPlayer_GetLastPlayedTimes_Response'] = _CPLAYER_GETLASTPLAYEDTIMES_RESPONSE
DESCRIPTOR.message_types_by_name['CPlayer_AcceptSSA_Request'] = _CPLAYER_ACCEPTSSA_REQUEST
DESCRIPTOR.message_types_by_name['CPlayer_AcceptSSA_Response'] = _CPLAYER_ACCEPTSSA_RESPONSE
DESCRIPTOR.message_types_by_name['CPlayer_LastPlayedTimes_Notification'] = _CPLAYER_LASTPLAYEDTIMES_NOTIFICATION
DESCRIPTOR.message_types_by_name['CPlayerClient_GetSystemInformation_Request'] = _CPLAYERCLIENT_GETSYSTEMINFORMATION_REQUEST
DESCRIPTOR.message_types_by_name['CClientSystemInfo'] = _CCLIENTSYSTEMINFO
DESCRIPTOR.message_types_by_name['CPlayerClient_GetSystemInformation_Response'] = _CPLAYERCLIENT_GETSYSTEMINFORMATION_RESPONSE

class CPlayer_GetGameBadgeLevels_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYER_GETGAMEBADGELEVELS_REQUEST

  # @@protoc_insertion_point(class_scope:CPlayer_GetGameBadgeLevels_Request)

class CPlayer_GetGameBadgeLevels_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Badge(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE

    # @@protoc_insertion_point(class_scope:CPlayer_GetGameBadgeLevels_Response.Badge)
  DESCRIPTOR = _CPLAYER_GETGAMEBADGELEVELS_RESPONSE

  # @@protoc_insertion_point(class_scope:CPlayer_GetGameBadgeLevels_Response)

class CPlayer_GetLastPlayedTimes_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYER_GETLASTPLAYEDTIMES_REQUEST

  # @@protoc_insertion_point(class_scope:CPlayer_GetLastPlayedTimes_Request)

class CPlayer_GetLastPlayedTimes_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Game(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME

    # @@protoc_insertion_point(class_scope:CPlayer_GetLastPlayedTimes_Response.Game)
  DESCRIPTOR = _CPLAYER_GETLASTPLAYEDTIMES_RESPONSE

  # @@protoc_insertion_point(class_scope:CPlayer_GetLastPlayedTimes_Response)

class CPlayer_AcceptSSA_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYER_ACCEPTSSA_REQUEST

  # @@protoc_insertion_point(class_scope:CPlayer_AcceptSSA_Request)

class CPlayer_AcceptSSA_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYER_ACCEPTSSA_RESPONSE

  # @@protoc_insertion_point(class_scope:CPlayer_AcceptSSA_Response)

class CPlayer_LastPlayedTimes_Notification(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYER_LASTPLAYEDTIMES_NOTIFICATION

  # @@protoc_insertion_point(class_scope:CPlayer_LastPlayedTimes_Notification)

class CPlayerClient_GetSystemInformation_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYERCLIENT_GETSYSTEMINFORMATION_REQUEST

  # @@protoc_insertion_point(class_scope:CPlayerClient_GetSystemInformation_Request)

class CClientSystemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class CPU(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CCLIENTSYSTEMINFO_CPU

    # @@protoc_insertion_point(class_scope:CClientSystemInfo.CPU)

  class VideoCard(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CCLIENTSYSTEMINFO_VIDEOCARD

    # @@protoc_insertion_point(class_scope:CClientSystemInfo.VideoCard)
  DESCRIPTOR = _CCLIENTSYSTEMINFO

  # @@protoc_insertion_point(class_scope:CClientSystemInfo)

class CPlayerClient_GetSystemInformation_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CPLAYERCLIENT_GETSYSTEMINFORMATION_RESPONSE

  # @@protoc_insertion_point(class_scope:CPlayerClient_GetSystemInformation_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')
_CPLAYER_GETLASTPLAYEDTIMES_REQUEST.fields_by_name['min_last_played'].has_options = True
_CPLAYER_GETLASTPLAYEDTIMES_REQUEST.fields_by_name['min_last_played']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030?The most recent last-played time the client already knows about')

_PLAYER = _descriptor.ServiceDescriptor(
  name='Player',
  full_name='Player',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), '\202\265\030)A service for accessing Steam player data'),
  serialized_start=1553,
  serialized_end=2046,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGameBadgeLevels',
    full_name='Player.GetGameBadgeLevels',
    index=0,
    containing_service=None,
    input_type=_CPLAYER_GETGAMEBADGELEVELS_REQUEST,
    output_type=_CPLAYER_GETGAMEBADGELEVELS_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030QReturns the Steam Level of a user, the Badge level for the game, and if it\'s foil'),
  ),
  _descriptor.MethodDescriptor(
    name='ClientGetLastPlayedTimes',
    full_name='Player.ClientGetLastPlayedTimes',
    index=1,
    containing_service=None,
    input_type=_CPLAYER_GETLASTPLAYEDTIMES_REQUEST,
    output_type=_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030*Gets the last-played times for the account'),
  ),
  _descriptor.MethodDescriptor(
    name='AcceptSSA',
    full_name='Player.AcceptSSA',
    index=2,
    containing_service=None,
    input_type=_CPLAYER_ACCEPTSSA_REQUEST,
    output_type=_CPLAYER_ACCEPTSSA_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030\031User is accepting the SSA'),
  ),
])

class Player(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _PLAYER
class Player_Stub(Player):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _PLAYER


_PLAYERCLIENT = _descriptor.ServiceDescriptor(
  name='PlayerClient',
  full_name='PlayerClient',
  file=DESCRIPTOR,
  index=1,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), '\202\265\030&Steam player data client notifications\300\265\030\002'),
  serialized_start=2049,
  serialized_end=2452,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyLastPlayedTimes',
    full_name='PlayerClient.NotifyLastPlayedTimes',
    index=0,
    containing_service=None,
    input_type=_CPLAYER_LASTPLAYEDTIMES_NOTIFICATION,
    output_type=steammessages_unified_base_pb2._NORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030;Notification from server to client of more recent play time'),
  ),
  _descriptor.MethodDescriptor(
    name='GetSystemInformation',
    full_name='PlayerClient.GetSystemInformation',
    index=1,
    containing_service=None,
    input_type=_CPLAYERCLIENT_GETSYSTEMINFORMATION_REQUEST,
    output_type=_CPLAYERCLIENT_GETSYSTEMINFORMATION_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\202\265\030LRequest from the server to the client for information about the users system'),
  ),
])

class PlayerClient(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _PLAYERCLIENT
class PlayerClient_Stub(PlayerClient):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _PLAYERCLIENT

# @@protoc_insertion_point(module_scope)