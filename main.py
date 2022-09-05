import telebot
from telebot import types
import chord_extract
import song_search
import re

with open("passcode.tx", 'r') as text:
    passcode = text.readline()
bot = telebot.TeleBot(passcode)


@bot.message_handler(commands=['start'])
def start(message):
    # Вывод приветственного сообщения при старте бота
    mess = 'Привет, <b>{name} {lastname}</b>'.format(name=message.from_user.first_name,
                                                     lastname=message.from_user.last_name)
    mess2 = 'Поиск песни (по названию, исполнителю):'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, mess2, parse_mode='html')
    bot.send_message(731694174, 'Пользователь {} (ID : {}) зашел в бота'.format(message.from_user.first_name,
                                                                                message.chat.id))  # Интерфейс для вывода ошибок


song_list_by_user = {}
song_list = []


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    text_message = message.text.lower()
    global song_list_by_user
    if not re.fullmatch(r'\b[\d_].*', text_message):
        # Если отправленный текст начинается с буквы, начать поиск песни
        song_list_by_user[message.chat.id] = song_search.listmake(text_message)
        if len(song_list_by_user[message.chat.id]) > 4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            k = 0
            songs_name = song_search.listpart_print(song_list_by_user[message.chat.id][k * 5:(k + 1) * 5], k)
            songs_name = [types.KeyboardButton(songs_name[i]) for i in range(len(songs_name))]
            markup.add(songs_name[0], songs_name[1], songs_name[2], songs_name[3], songs_name[4])
            bot.send_message(message.chat.id, 'Песни', parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Ничего не найдено', parse_mode='html')

    elif re.fullmatch(r'\b\d.*', text_message):
        # Если отправленный текст начинается с цифры, произвести вывод аккордов
        num = int(text_message[0]) - 1
        chords = chord_extract.main(song_list_by_user[message.chat.id][num][1].attrib['href'])
        bot.send_message(message.chat.id, chords, parse_mode='html')

    elif re.fullmatch(r'\b_.*', text_message):
        # Если отправленный текст начинается с "_", начать работу с командами
        print()

    else:
        bot.send_message(message.chat.id, 'I don\'t understand you, {}'.format(message.from_user.first_name),
                         parse_mode='html')


bot.polling(none_stop=True)
