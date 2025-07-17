import telebot

# Bot Token
BOT_TOKEN = '7824962565:AAECzNSYsu7eoGLQpElZ9fCVqBAAoxnlWRA'

# Admin Username
ADMIN_USERNAME = '@omyahackerroffical'

bot = telebot.TeleBot(BOT_TOKEN)

# Welcome Message
welcome_msg = """
👋 Welcome to BGMI Hack Bot 🛡️
Get Safe, Verified Hacks for BGMI! 🚀

Type /pricing to see available hacks.
Type /proof to see proof of our work.
Type /buy to purchase hacks.
Type /contact for support.

🚨 Disclaimer 🚨
For Educational Purpose Only. We don't promote scams or illegal use. Use at your own risk!
"""

# Pricing Info
pricing_info = """
🏷️ Hack Subscription Plans:

1️⃣ 1 Day Hack - ₹100
🔗 https://t.me/omyahackerr/17959

2️⃣ 2 Week Hack + Scanner - ₹450
🔗 https://t.me/omyahackerr/17960

3️⃣ 3 Month Hack - ₹800
🔗 https://t.me/omyahackerr/17957
"""

# Proof Links
proof_info = """
📸 Proof of Our Hacks:

https://t.me/omyahackerr/17951
https://t.me/omyahackerr/17914
https://t.me/omyahackerr/17906
https://t.me/omyahackerr/17900
"""

# Contact Info
contact_info = """
📞 Contact Us:
Telegram: https://t.me/Omya_hackerr
WhatsApp: https://wa.me/+919112372706
Instagram: https://www.instagram.com/omyahackerr
"""

# Commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_msg)

@bot.message_handler(commands=['pricing'])
def send_pricing(message):
    bot.reply_to(message, pricing_info)

@bot.message_handler(commands=['proof'])
def send_proof(message):
    bot.reply_to(message, proof_info)

@bot.message_handler(commands=['contact'])
def send_contact(message):
    bot.reply_to(message, contact_info)

# Buy Command
@bot.message_handler(commands=['buy'])
def send_buy_info(message):
    buy_info = """
🛒 Buy Hack Instructions:

1. Choose your Plan (/pricing)
2. Pay via QR Code or UPI.
3. Send Payment Proof to Admin.
4. Receive your Hack APK link!

For Payment & Support, contact:
Telegram: https://t.me/Omya_hackerr
"""
    bot.reply_to(message, buy_info)

bot.polling()
