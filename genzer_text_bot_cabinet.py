import telebot
import openpyxl
a = False
text_about_us = "Generation Z (GenZer) - it-кластер для дітей та підлітків нового покоління. Наші викладачі допоможуть Вашій дитині перетворити свої здібності та захоплення у професію мрії. Саме тут Ваша дитина зможе просто і захоплююче освоювати нові напрямки в комп'ютерній сфері, дізнатися масу корисної інформації і знайти нових друзів-однодумців з якими вивчення пройде неймовірно весело і цікаво! Сучасна методика викладання, новітнє технологічне та програмне забезпечення, висококваліфіковані наставники та заняття, які будуються на практиці - саме те, що потрібно для успішного старту в ІТ. Ми гордимося тим, що 85% наших студентів приходять до нас за рекомендаціями від знайомих та із задоволенням відвідують заняття!"
keyboard_menu = telebot.types.ReplyKeyboardMarkup()
keyboard_menu.row("Новини","Розклад")
keyboard_menu.row("Викладачі","Про Нас")
keyboard_teach = telebot.types.ReplyKeyboardMarkup()
keyboard_teach.row("Тетяна Климчук","Олександр Музиченко")
keyboard_teach.row("Юрій Панченко","Євген Солоп")
keyboard_teach.row("Олександр Паршуков","Альона Повисок")
keyboard_teach.row("Микола Павленко")
keyboard_teach.row("<--- Назад")
bot = telebot.TeleBot('915489974:AAGL39ZFY0YMiGhBelUyApqiET7d7O1z8eU')
@bot.message_handler(commands = ['start'])
def snoopie(message):
    bot.send_message(message.from_user.id,"добрий день,виберіть кнопку",reply_markup = keyboard_menu)
@bot.message_handler(content_types = ['text'])
def yssup(message):
    global a
    if message.text == "Новини":
        bot.send_message(message.from_user.id,"Ви натиснули кнопку  Новини",reply_markup = keyboard_menu)
    if message.text == "Розклад":
        wb = openpyxl.load_workbook(filename = 'people.xlsx')
        List = wb['sheet1']
        coloumn_a = List['A']
        for i in range(2,len(coloumn_a)+1):
            if List['A'+str(i)].value == message.from_user.id:
                if List['D'+str(i)].value != 0:
                    print(str(List['D'+str(i)].value))
                    bot.send_message(message.from_user.id,str(List['D'+str(i)].value))
                if List['E'+str(i)].value != 0:
                    bot.send_message(message.from_user.id,str(List['E'+str(i)].value))
                if List['F'+str(i)].value != 0:
                    bot.send_message(message.from_user.id,str(List['F'+str(i)].value))
    if message.text == "Викладачі":
        bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAJhg161Xl_9xN3NWshGdxqG5WvFA1MpAAIsAAN94rIVYHIAATpgviAGGQQ")
        msg = bot.send_message(message.from_user.id,"Ви натиснули кнопку Викладачі",reply_markup = keyboard_teach)
        bot.register_next_step_handler(msg , teacher)
        a = True
    if a:
        msg = bot.send_message(message.from_user.id,"",reply_markup = keyboard_teach)
        bot.register_next_step_handler(msg , teacher)
    if message.text == "Про Нас":
        bot.send_photo(message.from_user.id,open('foto.png','rb'))
        bot.send_message(message.from_user.id,text_about_us)
def teacher(message):
    global a
    if message.text == "<--- Назад":
        msg = bot.send_message(message.from_user.id,"В повернулись до меню",reply_markup = keyboard_menu)
        bot.register_next_step_handler(msg, yssup)
        a = False
    if message.text == "Тетяна Климчук":
        bot.send_message(message.from_user.id,"Т.К.")
    if message.text == "Олександр Музиченко":
         bot.send_message(message.from_user.id,"O.M.")
    if message.text == "Юрій Панченко":
         bot.send_message(message.from_user.id,"Ю.П.")
    if message.text == "Євген Солоп":
         bot.send_message(message.from_user.id,"Є.С.")
    if message.text == "Олександр Паршуков":
         bot.send_message(message.from_user.id,"О.П.")
    if message.text == "Альона Повисок":
         bot.send_message(message.from_user.id,"A.П.")
    if message.text == "Микола Павленко":
         bot.send_message(message.from_user.id,"М.П.")
bot.polling()
