from django.urls import re_path

from . import consumers

websocket_urlpattern=[
    re_path(r"ws/metro_gpt/room",consumers.ChatConsumer.as_asgi()),

]