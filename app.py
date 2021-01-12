import telebot, json
from parser_vk_bot.db.CRUD import show_url
bot = telebot.TeleBot('1251383389:AAHHmiSpeiyqCj6lkN7ctxqsg_zI4zYmsf8')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.add('Привет', 'Следующий пост')
idz = 1


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


def ids():
    global idz
    idz += 1
    return idz


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        telebot.types.ReplyKeyboardRemove(True)
        a = telebot.types.ReplyKeyboardMarkup(True)
        a.row("Следующий пост")
        return bot.send_message(message.chat.id, show_url(idz),reply_markup=a)
    elif message.text == "Следующий пост":
        return bot.send_message(message.chat.id, show_url(ids()))
    else:
        return bot.send_message(message.chat.id, "Неверная команда")


bot.polling()