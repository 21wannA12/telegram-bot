import telebot
from telebot import types


bot = telebot.TeleBot("8094094842:AAE3vjkKgUKOcPC6kx9B4ynO2XQH21VZ5MA")
@bot.message_handler(commands=["start"])
def start(message): #функция, которая выполняется при вводе команд написанных выше
    markup = types.InlineKeyboardMarkup() #создание и вид кнопки
    button = types.InlineKeyboardButton("Steam", url="https://steamcommunity.com/id/kwcry/")
    button_2 = types.InlineKeyboardButton("Telegram Channel", url="https://t.me/roomtokkwcv")
    button_3 = types.InlineKeyboardButton("GitHub", url="https://github.com/21wannA12")
    button_4 = types.InlineKeyboardButton("Discord", url="http://discordapp.com/users/762727236519854080")
    button_5 = types.InlineKeyboardButton("Telegram Account ", url="http://t.me/kw3ry")
    markup.row(button_2, button_5)
    markup.row(button_3, button_4, button)

    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}.")
    bot.send_message(message.chat.id, f"Ниже можно увидеть кнопки с помощью которых вы можете перейти на мои другие аккаунты помимо Telegram.", reply_markup=markup)

bot.polling(none_stop=True)