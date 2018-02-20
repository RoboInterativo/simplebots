#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
ConversationHandler)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

ANSW1 = range(1)
def start(bot, update):
    reply_keyboard = [['Хорошо', 'Плохо', 'ХЗ']]

    update.message.reply_text(
        'Как дела?.\n\n',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ANSW1
def answ1(bot, update):
    user = update.message.from_user
    text = update.message.text
    update.message.reply_text('Ваши дела идут ' +text,
                              reply_markup=ReplyKeyboardRemove())

    return 
def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Пока.',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater("531541258:AAEVPYrpZ5Y1BvJtxcxodXo72_H0UQEx0JM")
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ANSW1: [RegexHandler('^(Хорошо|Плохо|ХЗ)$', answ1)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
        )
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

    
if __name__ == '__main__':
    main()
