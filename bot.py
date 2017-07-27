from telegram.ext import Updater
from telegram.ext import CommandHandler
from divises import obtenirEquivalencia

updater = Updater(token='AQUI HI VA EL TEU TOKEN')
dispatcher = updater.dispatcher

def saluda(bot, update):
    missatge = 'Sóc aquí :)'
    bot.sendMessage(chat_id=update.message.chat_id, text=missatge)

def saluda_nom(bot, update, args):
    missatge = 'Hola '+args[0]+'!'
    bot.sendMessage(chat_id=update.message.chat_id, text=missatge)

def conversio(bot, update, args):
    missatge = obtenirEquivalencia(args[0], args[1], args[2])
    bot.sendMessage(chat_id=update.message.chat_id, text=missatge)

handlers = [CommandHandler('saluda', saluda), 
	    CommandHandler('saluda_nom', saluda_nom, pass_args=True), 
            CommandHandler('conversio', conversio, pass_args=True)]

for handler in handlers:
	dispatcher.add_handler(handler)

updater.start_polling()



