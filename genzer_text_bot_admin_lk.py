import telebot
import openpyxl
keyboard_admin = telebot.types.ReplyKeyboardMarkup()
keyboard_admin.row("Создать рассылку")
keyboard_mailing = telebot.types.ReplyKeyboardMarkup()
keyboard_mailing.row("Отменить рассылку")
bot = telebot.TeleBot('915489974:AAGL39ZFY0YMiGhBelUyApqiET7d7O1z8eU')
@bot.message_handler(commands = ['start'])
def meet(message):
    wb = openpyxl.load_workbook(filename = 'people.xlsx')
    List = wb["sheet1"]
    column_a = List['A']
    for i in range(1,len(column_a)+1):
        if str(List['A'+str(i)].value) == str(message.from_user.id):
            bot.send_message(message.from_user.id,"Привітання адміну",reply_markup = keyboard_admin)
@bot.message_handler(content_types = ['text'])
def menu(message):
    if message.text == "Создать рассылку":
        msg = bot.send_message(message.from_user.id, "Введіть повідомлення, а потім натисніть відправити",reply_markup = keyboard_mailing)
        bot.register_next_step_handler(msg , mailing)
def mailing(message):
    if message.text == "Отменить рассылку":
        msg = bot.send_message(message.from_user.id, "Рассылку отменено",reply_markup = keyboard_admin)
        bot.register_next_step_handler(msg , menu)
    else:
        wb = openpyxl.load_workbook(filename = 'people.xlsx')
        List = wb["sheet1"]
        column_a = List['A']
        for i in range(2,len(column_a)+1):
            bot.send_message(List['A'+str(i)].value,message.text)
            print(List['A'+str(i)].value)
        msg = bot.send_message(message.from_user.id, "Рассылку закончена",reply_markup = keyboard_admin)
        bot.register_next_step_handler(msg , menu)
bot.polling()
            
