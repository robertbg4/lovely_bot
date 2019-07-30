import mongoengine as db


class Message(db.Document):
    counter = db.SequenceField(collection_name='message.counters')
    text = db.StringField(required=True)

    def send(self, bot, chat_id):
        bot.send_message(chat_id=chat_id, text=self.text)
