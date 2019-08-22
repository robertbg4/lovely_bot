import random

from config import dispatcher, blog_id, admin_id
from models import Message

try:
    sleep(random.randint(0, 3*60*60))
    message = Message.objects.get(counter=random.randrange(1, Message.objects.count() + 1))
    message.send(dispatcher.bot, blog_id)
except Exception as e:
    dispatcher.bot.send_message(chat_id=admin_id, text=e)
