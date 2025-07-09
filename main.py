import telebot
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! 📈 Signal bot ishga tushdi.\nЗдравствуйте! Бот сигналов запущен.")

print("✅ Bot started polling...")
bot.polling()
