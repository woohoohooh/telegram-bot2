from config import token
import telebot
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardMarkup('Как дела?', callback_data='question_1')
    item2 = types.InlineKeyboardMarkup('Пока', callback_data='goodbye')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

bot.polling()