"""
ASGI config for configuration project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from events.consumers import OrdersConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuration.settings")

ws_patterns = [
    path('ws/streams/<int:pk>/', OrdersConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(ws_patterns)
    )
})
