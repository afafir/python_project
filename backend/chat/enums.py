from django.db.models import TextChoices


class MessengerType(TextChoices):
    TELEGRAM = "TELEGRAM", "Телеграм"
    VK = (
        "VK",
        "Вконтакте",
    )
