import telebot
from telebot import types


bot = telebot.TeleBot("ВАШ ТОКЕН")
@bot.message_handler(commands=["start"])
def start(message): 
    markup = types.InlineKeyboardMarkup() 
    button = types.InlineKeyboardButton("Steam", url="ВАША ССЫЛКА")
    button_2 = types.InlineKeyboardButton("Telegram Channel", url="ВАША ССЫЛКА")
    button_3 = types.InlineKeyboardButton("GitHub", url="ВАША ССЫЛКА")
    button_4 = types.InlineKeyboardButton("Discord", url="ВАША ССЫЛКА")
    button_5 = types.InlineKeyboardButton("Telegram Account ", url="ВАША ССЫЛКА")
    markup.row(button_2, button_5)
    markup.row(button_3, button_4, button)

    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}.")
    bot.send_message(message.chat.id, f"Ниже можно увидеть кнопки с помощью которых вы можете перейти на мои другие аккаунты помимо Telegram.", reply_markup=markup)


bot.polling(none_stop=True)
