from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from ChannelApp.consumers import TokenAuthConsumer
from ChannelApp.middlewares import TokenAuthMiddleWare

application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleWare(
            AllowedHostsOriginValidator(
                URLRouter(
                [path("", TokenAuthConsumer.as_asgi())]
                )
            )
        )
    }
)