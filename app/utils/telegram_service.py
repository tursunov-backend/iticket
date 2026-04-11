from telegram import Bot

from app.models import Event
from app.core.config import settings


class TelegramService:
    def __int__(self):
        self.bot = Bot(settings.telegram_bot_token)

    def send_event(self, event: Event):
        self.bot.send_message(
            chat_id=settings.telegram_channel,
            text=f"{event.title} at {event.date}",
        )
