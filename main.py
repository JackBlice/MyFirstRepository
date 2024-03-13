import telebot
from telebot import types
import random

token = '6448241650:AAF3jNuzPjwfhhXdjRiRZZqCUhsdrlUTwwk'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Играть')
btn2 = types.KeyboardButton('Нет, я пас')
keyboard.add(btn1, btn2)


@bot.message_handler(commands = ['start', 'game'])

def star_message(message):
    bot_message = bot.send_message(message.chat.id, 'Привет Чемпион, начнем игру?', reply_markup = keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 9 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
        number = random.randint(1, 9)
        print(number)
        game(message, 5, number)
    elif message.text == 'Нет, я пас':
        bot.send_message(message.chat.id, 'Нет так нет, пока')
    else:
        bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильный ответ\n Введи снова: ', reply_markup = keyboard)
        bot.register_next_step_handler(bot_message, check_answer)


def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Угадай число!')
    bot.register_next_step_handler(message_bot, chek_number, attempts-1, number)


def chek_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Ты победил')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'U tebya nol popytok, ty proigral')
    else:
        bot.send_message(message.chat.id, f'Ty proigral, colichestvo tvoih popytok:{attempts}')
        game(message, attempts, number)

















bot.polling()

































































































