from rest_framework import serializers


class ChatMessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    chat_id = serializers.IntegerField()


class ChatMessageCreateSerializer(serializers.Serializer):
    text = serializers.CharField()
    extra_data = serializers.JSONField()
    messenger = serializers.CharField()


class ChatMessageListSerializer(serializers.Serializer):
    text = serializers.CharField()
    sent_at = serializers.DateTimeField(source="created_at")
    local = serializers.SerializerMethodField()

    def get_local(self, obj):
        if obj.is_auto_generated:
            return True
        if hasattr(obj, "local"):
            return obj.local
        else:
            return bool(obj.sent_by_id)


class ChatSerializer(serializers.Serializer):
    title = serializers.CharField()
    messenger = serializers.CharField()
    extra_data = serializers.JSONField()
    id = serializers.IntegerField()
    messages = ChatMessageListSerializer(many=True)
