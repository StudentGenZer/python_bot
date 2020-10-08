import telebot
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row("Hello","Goodbay")
keyboard_new = telebot.types.ReplyKeyboardMarkup()
keyboard_new.row("Back")
bot = telebot.TeleBot('946264460:AAHpoSg7yTCi8xbgjjpRc8o1HDxrmecnQ2I')
@bot.message_handler(commands = ['start'])
def rip(message):
    bot.send_message(message.from_user.id,"Hello,world!!111",reply_markup = keyboard)
@bot.message_handler(content_types = ["text"])
def send(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id,"Hello< how are you",reply_markup = keyboard_new)
    elif message.text == "Goodbay":
        bot.send_message(message.from_user.id,"Goodbay my creaters")
    elif message.text == "Back":
        bot.send_message(message.from_user.id, "dfg", reply_markup = keyboard)
    else:
        bot.send_message(message.from_user.id,"Error")
bot.polling()

    
