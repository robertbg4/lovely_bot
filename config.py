import configparser

from mongoengine import connect
from telegram import ext

config = configparser.RawConfigParser()
config.read('config.ini')


updater = ext.Updater(token=config['main']['TELEGRAM_BOT_TOKEN'])
dispatcher = updater.dispatcher

admin_id = int(config['main']['ADMIN_ID'])
if not admin_id:
    raise ValueError("Couldn't load without admin id")
blog_id = config['main']['BLOG_ID']
if not blog_id:
    raise ValueError("Couldn't load without blog id")

client = connect(host=config['main']['DB_HOST'])
