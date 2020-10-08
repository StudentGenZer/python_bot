import telebot
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row("Реєстрація","Вхід")
bot = telebot.TeleBot('915489974:AAGL39ZFY0YMiGhBelUyApqiET7d7O1z8eU')
log = True
reg = True
a = ""
b = ""
@bot.message_handler(commands = ['start'])
def rip(message):
    global log
    file = open("text.txt",'r')
    bot.send_message(message.from_user.id,"Вітаю! До ваших послуг телеграм бот GenerationZ",reply_markup = keyboard)
    for line in file:
        if str(message.from_user.id)+"\n" == line:
            log = False     
    file.close()
    if log:
        file = open("text.txt","a")
        file.write(str (message.from_user.id)+"\n")
        file.close()



@bot.message_handler(commands = ['reg'])
def sup(message):
    bot.send_message(message.from_user.id,"Введіть ваше прізвіще та ім'я!")
@bot.message_handler(commands = ['log'])
def pus(message):
    bot.send_message(message.from_user.id,"Вхід")
        
@bot.message_handler(content_types = ['text'])
def pir(message):
    global a
    global reg
    global b
    if message.from_user.id == 625462305:
        a = message.text
        file = open("text.txt","r")
        for line in file:
            bot.send_message(int(line),a)
bot.polling()
