# gd_app/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<room_code>\w+)/$', consumers.VideoConsumer.as_asgi()),
]