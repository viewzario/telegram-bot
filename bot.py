from pyrogram import Client, filters
import os
from apscheduler.schedulers.background import BackgroundScheduler

# 🔹 Получаем данные из переменных окружения
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# 🔹 Создаём бота
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 🔹 Обработчик команды /start
@app.on_message(filters.command("start"))
def start_message(client, message):
    message.reply_text(
        "Привет! Я помогу тебе развить мышление и восприятие. 🚀\n\n"
        "Напиши /help, чтобы узнать больше."
    )

# 🔹 Запуск бота
if __name__ == "__main__":
    app.run()
