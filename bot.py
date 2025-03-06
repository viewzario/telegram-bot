from pyrogram import Client, filters
import time
from apscheduler.schedulers.background import BackgroundScheduler

# 🔹 Вставь свои данные (API ID, API Hash, Bot Token)
import os

api_id = int(os.getenv("API_ID"))  # Читаем API ID из переменных окружения
api_hash = os.getenv("API_HASH")  # Читаем API Hash из переменных окружения
bot_token = os.getenv("BOT_TOKEN")  # Читаем Bot Token из переменных окружения

# 🔹 Создаём бота
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 🔹 Хранение подписчиков (простой вариант в памяти)
subscribers = set()

# 🔹 Обработчик команды /start
@app.on_message(filters.command("start"))
def start_message(client, message):
    message.reply_text(
        "Привет! Я помогу тебе развить мышление и восприятие. 🚀\n\n"
        "Напиши /help, чтобы узнать больше."
    )

# 🔹 Обработчик команды /help
@app.on_message(filters.command("help"))
def help_message(client, message):
    message.reply_text(
        "ℹ Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Список команд\n"
        "/subscribe - Подписаться на инсайты 📩\n"
        "/unsubscribe - Отписаться от рассылки"
    )

# 🔹 Команда /subscribe (подписка на рассылку)
@app.on_message(filters.command("subscribe"))
def subscribe(client, message):
    user_id = message.from_user.id
    subscribers.add(user_id)
    message.reply_text("✅ Ты подписался на ежедневную рассылку инсайтов! 📩")

# 🔹 Команда /unsubscribe (отписка)
@app.on_message(filters.command("unsubscribe"))
def unsubscribe(client, message):
    user_id = message.from_user.id
    if user_id in subscribers:
        subscribers.remove(user_id)
        message.reply_text("❌ Ты отписался от рассылки.")
    else:
        message.reply_text("Ты не был подписан.")

# 🔹 Функция для отправки сообщений подписчикам
def send_daily_insight():
    if subscribers:
        insight = "💡 Инсайт дня: Вселенная не такая, какой ты её видишь. Она такая, какой ты её осознаёшь."
        for user_id in subscribers:
            try:
                app.send_message(user_id, insight)
            except Exception as e:
                print(f"Ошибка отправки {user_id}: {e}")

# 🔹 Запуск планировщика
scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_insight, "interval", hours=24)  # Авторассылка каждые 24 часа
scheduler.start()

# 🔹 Запуск бота
app.run()
