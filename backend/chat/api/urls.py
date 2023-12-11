from django.urls import path, include
from rest_framework.routers import SimpleRouter

from chat.api.views import ChatViewSet, ChatMessageViewSet

app_name = "chat"

router = SimpleRouter()
router.register("chats", ChatViewSet, "chats")
router.register("messages", ChatMessageViewSet, "messages")

urlpatterns = [path("", include(router.urls))]
