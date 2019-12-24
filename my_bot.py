from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging
import settings

#Настройка вывода логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(bot, update):
    text = 'Вызвана команда /start'
    logging.info(text)
    update.message.reply_text('Вы выполнили комманду /start') #Позволяет ответить пользователю на комманду

def talk_to_me(bot, update):
    user_text = f'Привет {update.message.chat.first_name}! Ты мне написал: {update.message.text}'#Пример как можно вытащить из update.message данные о пользователе
    logging.info('Пользователь: %s, Чат ID: %s, Сообщение: %s', update.message.chat.first_name, update.message.chat.id, update.message.text)
    #print(update.message)#очень полезная комманда, мы можем узнать очень много информации о пользователе
    update.message.reply_text(user_text)

def main ():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))# вызов обработчика комманды /start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))# вызов обработчика текста введенного от пользователя
    mybot.start_polling()#Команда начни проверять  сообщения
    mybot.idle()#Комманда которая запускает наш бот и он будет работать до тех пор пока его не остановят
main()