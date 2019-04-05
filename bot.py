import telegram
from telegram.ext import CommandHandler
from updater import updater

import random
import warnings

from datetime import date
import calendar

today_adj = None



def get_adjective(start_letter):
    """
    start_letter: a lower_case letter
    """
    try:
        with open(start_letter+".txt", 'r') as f:
            lines = int(f.readline())
            index = random.randint(0, lines)
            for x in range(index):
                f.readline()
            return f.readline().strip()
    except:
        warnings.warn("Error: could not get word.")
        return ""

def get_day_name():
    """
    returns day name (uppercased first letter)
    """
    return calendar.day_name[date.today().weekday()]

def get_day_letter():
    """
    returns starting letter of weekday name lowercased
    """
    day_name = get_day_name()
    return day_name[0].lower()

def get_today_name():
    global today_adj
    if today_adj is None:
        today_adj = get_adjective(get_day_letter())
    elif today_adj[0] != get_day_letter():
        today_adj = get_adjective(get_day_letter())
    today_name = f"{today_adj.capitalize()} {get_day_name()}"
    return today_name

def today(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=get_today_name())

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="/today to get today's name")

def main():
    #setup
    global today_adj
    today_adj = get_adjective(get_day_letter())
    dispatcher = updater.dispatcher

    today_handler = CommandHandler('today', today)
    dispatcher.add_handler(today_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()