from telegram.ext import Updater
from telegram.ext import CommandHandler
def start(bot, update):
   bot.send_message(chat_id=update.message.chat_id, text=
   "I'm a bot, please talk to me!")

tok="531541258:AAEVPYrpZ5Y1BvJtxcxodXo72_H0UQEx0JM"
updater = Updater(token=tok)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
