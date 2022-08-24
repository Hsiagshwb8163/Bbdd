import telebot

bot = telebot.TeleBot("5301993742:AAE_Z1iRlcYekhyf64Ulb4cImTwR2MMRXPk")

@bot.message_handler(commands=['start'])
def aaa(m):
    bot.send_message(m.chat.id,"Hi")
    print("Someone Called a message")

bot.polling()
