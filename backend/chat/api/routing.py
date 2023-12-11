from django.urls import path

from chat.api.consumers import ChatConsumer

websocket_urlpatterns = [path("api/messaging/ws/", ChatConsumer.as_asgi())]
