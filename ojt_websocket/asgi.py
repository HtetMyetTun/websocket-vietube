"""
ASGI config for ojt_websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter,URLRouter

import simple_chat.routing

import metro_gpt.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ojt_websocket.settings')

application = get_asgi_application()

application=ProtocolTypeRouter(
    {
        "http":get_asgi_application(),
        #Just HTTP for now.(We can add other protocol later.)

        "websocket":URLRouter(
            simple_chat.routing.websocket_urlpattern+
            metro_gpt.routing.websocket_urlpattern
            
        )
    }
)