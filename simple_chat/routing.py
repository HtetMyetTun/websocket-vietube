from django.urls import re_path

from . import consumers

websocket_urlpattern=[
    re_path(r"ws/simple_chat/room1",consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/simple_chat/group_chat/(?P<room_name>\w+)/",consumers.GroupChatConsumer.as_asgi()),
]