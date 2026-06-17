from django.core.management.base import BaseCommand
from telegram_bot.bot import bot

class Command(BaseCommand):
    help = "Запускає Telegram‑бота"

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
