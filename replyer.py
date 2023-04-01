#import dependencies
import random
from random import randrange
from telegram.ext import Updater, MessageHandler, Filters

#reading file. use utf encoding(відкриває і читає текстовий файл)
with open('phrases.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    #split text with line breaks(розділяє на елементи по перенесенню рядка)
    lines = content.split('\n')

def reply(update, context):
    # Get the chat ID (отримання доступу до чату. через батю теж настроїти)
    chat_id = update.effective_chat.id
    
    #generating of rnd num. if its odd & > 8 then bot reply w/ rnd phrase(якщо непарне і > 8, то бот відповідає)
    if randrange(10) % 2 == 1 and randrange(10) >= 6:
        #rnd ph select(вибір випадкової фрази)
        reply_text = random.choice(lines)
        #replying(відповідь)
        context.bot.send_message(chat_id=chat_id, text=reply_text, reply_to_message_id=update.message.message_id)
def main():
    # bot token(токен)
    updater = Updater(token="6194775640:AAELa_L3UjAFm4iPxJruJwuXRAPT1b6tzDE", use_context=True)

    # Set up the message handler to respond to all messages(відповідь на будь-який тип повідомлення)
    message_handler = MessageHandler(Filters.text & ~Filters.command, reply, pass_chat_data=True)
    updater.dispatcher.add_handler(message_handler)

    # Start the bot.(стартуєм)
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or or bug(працює нескінченно до помилки чи примусового виходу)
    updater.idle()

if __name__ == '__main__':
    main()