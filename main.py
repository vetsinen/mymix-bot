import telebot
from telebot import types
# token for @bailandobot
bot = telebot.TeleBot("1093604140:AAGlTCUgzPSLZsJNrSDO_hrj54IGbveU7NU")

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
  blackpool: str = '''Вітання! Гра почалася. У MyMix тебе чекають нові знайомства і завдання по саморозвитку.
           Натисни на кнопку «Продовжити»
           Якщо ти не бачиш кнопку, натисни на іконку з чотирма квадратиками справа в рядку введення.
           Якщо зовсім нічого не зрозуміло, напиши /help потрібна допомога, і тобі допоможе жива людина'''
  bot.reply_to(message, blackpool)

@bot.message_handler(content_types=['text'])
def send_text(message: types.Message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Привіт, '+message.chat.username)
    elif message.text.lower() == 'прощавай':
        bot.send_message(message.chat.id, 'Прощавай, '+message.chat.username)
    else:
      bot.send_message(message.chat.id, 'Я лише тільки навчаюсь')

if __name__=='__main__':
  bot.polling()