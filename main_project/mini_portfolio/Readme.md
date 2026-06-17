

# MiniPortfolio

MiniPortfolio — це Django‑додаток для створення та перегляду портфоліо користувачів із інтеграцією Telegram‑бота.

## 🚀 Функціональність
- Реєстрація, вхід та вихід користувачів
- Додавання власних проєктів (назва, опис, картинка, посилання)
- Перегляд карток проєктів із Bootstrap‑оформленням
- Пагінація у стилі Bootstrap
- Запити на видалення проєктів
- Інтеграція з Telegram‑ботом (@mini_portfolio_django_bot):
  - Автор отримує повідомлення про створення проєкту
  - Адміни отримують повідомлення про запити на видалення
  - Підключення через команду `/start` у боті

## 📂 Структура
```
mini_portfolio/
├── mini_portfolio/        # головні налаштування Django
├── portfolio/             # додаток із моделями, views, шаблонами
├── telegram_bot/          # логіка Telegram‑бота
├── requirements.txt       # залежності
└── README.md              # документація
```

## ⚙️ Встановлення
1. Клонувати репозиторій:
   ```bash
   git clone https://github.com/yourusername/mini_portfolio.git
   cd mini_portfolio
   ```

2. Створити віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Встановити залежності:
   ```bash
   pip install -r requirements.txt
   ```

4. Виконати міграції:
   ```bash
   python manage.py migrate
   ```

5. Запустити сервер:
   ```bash
   python manage.py runserver
   ```

## 🤖 Telegram‑бот
1. Створити бота через [BotFather](https://t.me/BotFather) та отримати токен.  
2. Записати токен у файл `telegram_bot/telegram_config.py`:
   ```python
   TELEGRAM_BOT_TOKEN = "your_bot_token_here"
   APP_BASE_URL = "http://127.0.0.1:8000"
   ```
3. Запустити бота:
   ```bash
   python telegram_bot/bot.py
   ```
4. Користувачі підключаються через команду `/start` у @mini_portfolio_django_bot.

## 👨‍💻 Author
Oleksandr Zabolotnyi

https://github.com/Oleksandr-Zabo