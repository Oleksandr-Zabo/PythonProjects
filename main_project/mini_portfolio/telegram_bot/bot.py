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
    requests.post(f"{APP_BASE_URL}/connect-telegram/", json={
        "telegram_id": chat_id,
        "username": username
    })


# Показати список проєктів
@bot.message_handler(commands=['projects'])
def show_projects(message):
    chat_id = message.chat.id
    username = message.from_user.username
    
    try:
        # Отримуємо проєкти користувача
        response = requests.get(f"{APP_BASE_URL}/api/user-projects/{username}/")
        if response.status_code == 200:
            projects = response.json()
            if projects:
                msg = "Ваші проєкти:\n\n"
                for project in projects:
                    msg += f"📌 {project['title']}\n"
                    msg += f"🔗 {project['link']}\n"
                    msg += f"📅 {project['created_at']}\n\n"
                bot.send_message(chat_id, msg)
            else:
                bot.send_message(chat_id, "У вас поки немає проєктів.")
        else:
            bot.send_message(chat_id, "Не вдалося отримати проєкти.")
    except Exception as e:
        bot.send_message(chat_id, f"Помилка: {str(e)}")


# Показати запити на видалення
@bot.message_handler(commands=['requests'])
def show_delete_requests(message):
    chat_id = message.chat.id
    username = message.from_user.username
    
    try:
        # Отримуємо запити на видалення
        response = requests.get(f"{APP_BASE_URL}/api/delete-requests/")
        if response.status_code == 200:
            requests_data = response.json()
            if requests_data:
                msg = "Запити на видалення:\n\n"
                for req in requests_data:
                    msg += f"🗑️ Проєкт: {req['project_title']}\n"
                    msg += f"👤 Від: {req['user_username']}\n"
                    msg += f"📝 Причина: {req['reason']}\n"
                    msg += f"📅 {req['created_at']}\n\n"
                bot.send_message(chat_id, msg)
            else:
                bot.send_message(chat_id, "Немає активних запитів на видалення.")
        else:
            bot.send_message(chat_id, "Не вдалося отримати запити.")
    except Exception as e:
        bot.send_message(chat_id, f"Помилка: {str(e)}")


# Допомога
@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = """
🤖 MiniPortfolio Bot Commands:

/start - Підключити бота до вашого акаунту
/projects - Переглянути ваші проєкти
/requests - Переглянути запити на видалення
/help - Показати цю довідку
    """
    bot.send_message(message.chat.id, help_text)
