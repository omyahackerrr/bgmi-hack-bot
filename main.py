from keep_alive import keep_alive
keep_alive()
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "unknown")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello 👋\nThis bot is managed by @{OWNER_USERNAME}")

bot.infinity_polling()
