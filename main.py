import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "🇺🇿 Assalomu alaykum! 📈 Signal bot ishga tushdi.
🇷🇺 Здравствуйте! Бот сигналов запущен.")

bot.polling()
