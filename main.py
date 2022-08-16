import telebot
from telebot import types
import chord_extract
import song_search

with open("passcode.tx", 'r') as text:
    passcode = text.readline()
bot = telebot.TeleBot(passcode)


@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Привет, <b>{name} {lastname}</b>'.format(name=message.from_user.first_name,
                                                     lastname=message.from_user.last_name)
    mess2 = 'Поиск песни (по названию, исполнителю):'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Hello, bot!')
    btn2 = types.KeyboardButton('My ID')
    btn3 = types.KeyboardButton('Links')
    btn4 = types.KeyboardButton('Chords')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, mess, parse_mode='html')#, reply_markup=markup)
    bot.send_message(message.chat.id, mess2, parse_mode='html')

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Excellent photo!')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    text_message = message.text.lower()
    if text_message[0] != '_':
        songlist = song_search.listmake(text_message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        k = 0
        songs = song_search.listpart_print(songlist[k * 5:(k + 1) * 5], k)
        for i in range(len(songs)):
            songs[i] = types.KeyboardButton(songs[i])
        markup.add(songs[0], songs[1], songs[2], songs[3], songs[4])
        bot.send_message(message.chat.id, 'Песни', parse_mode='html', reply_markup=markup)
        # chords = chord_extract.main(url)
        # bot.send_message(message.chat.id, chords, parse_mode='html')


    elif text_message == 'back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Hello, bot!')
        btn2 = types.KeyboardButton('My ID')
        btn3 = types.KeyboardButton('Links')
        btn4 = types.KeyboardButton('Photo')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Let\'s try one more time?', parse_mode='html', reply_markup=markup)

    else:
        if text_message == 'hello, bot!':
            bot.send_message(message.chat.id, 'You are welcome!', parse_mode='html')
        elif text_message == 'my id':
            bot.send_message(message.chat.id,
                             '{}, your ID is {}'.format(message.from_user.first_name, message.from_user.id),
                             parse_mode='html')
        elif text_message == 'chords':
            chords = chord_extract.main()
            bot.send_message(message.chat.id, chords, parse_mode='html')
        elif text_message == 'google':
            markup_text = types.InlineKeyboardMarkup()
            markup_text.add(types.InlineKeyboardButton('Go to Google', url='https://google.com'))
            bot.send_message(message.chat.id, 'Let\'s go', reply_markup=markup_text)
        elif text_message == 'youtube':
            markup_text = types.InlineKeyboardMarkup()
            markup_text.add(types.InlineKeyboardButton('Go to YouTube', url='https://youtube.com'))
            bot.send_message(message.chat.id, 'Let\'s go', reply_markup=markup_text)
        elif text_message == 'codewars':
            markup_text = types.InlineKeyboardMarkup()
            markup_text.add(types.InlineKeyboardButton('Go to CodeWars', url='https://codewars.com'))
            bot.send_message(message.chat.id, 'Let\'s go', reply_markup=markup_text)
        elif text_message == 'кинопоиск':
            markup_text = types.InlineKeyboardMarkup()
            markup_text.add(types.InlineKeyboardButton('Go to КиноПоиск', url='https://hd.kinopoisk.ru/'))
            bot.send_message(message.chat.id, 'Let\'s go', reply_markup=markup_text)
        else:
            bot.send_message(message.chat.id, 'I don\'t understand you, {}'.format(message.from_user.first_name),
                             parse_mode='html')


bot.polling(none_stop=True)
