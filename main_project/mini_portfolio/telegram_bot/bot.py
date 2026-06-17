import telebot
import requests
from django.conf import settings
from .telegram_config import TELEGRAM_BOT_TOKEN, APP_BASE_URL

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


# Коли користувач натискає /start у боті
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username

    bot.send_message(chat_id, "Ви підключили MiniPortfolio. Ваш Telegram ID збережено.")

    # Надсилаємо дані у Django
    requests.post(f"{APP_BASE_URL}/api/connect-telegram/", json={
        "telegram_id": chat_id,
        "username": username
    })
