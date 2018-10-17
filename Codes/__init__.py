import telegram
import json
import time
import datetime
from Codes import Model
from Codes import AlertTime
from Codes import Web
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# TOKEN - #

TOKEN = "Your Token"

vaqt = Model.Vaqt()

def start(bot, update):
    update.message.reply_text("Assalomu aleykum --- /vaqt")
    user = {"ID" : update.message.chat.id}
    Model.UserModel.addUser('users.json',user)

def todayTimes(bot,update):
    update.message.reply_text(vaqt.getAll())

def echo(bot, update):
    update.message.reply_text(update.message.text)

    print("ID : " + str(update.message.chat.id) + "\n"
          "username : " + update.message.chat.username + "\n"
          "first_name : " + update.message.chat.first_name  + "\n"
          "Text : " + update.message.text)
    print()

def main():
    now = datetime.datetime.now()
    url = 'http://api.aladhan.com/v1/calendarByCity'
    data = {'country' : 'UZ','city' : 'Tashkent', 'method' : 3,'school' : 1,
            'tune' : '0,16,0,0,0,0,0,-11,0','year' : now.year,'month' : now.month}

    file_name = "users.json"
#   user = Model.UserModel()
#   user.ID = 4651
    #user = {"ID" : 4513}
    #Model.FileWorker.createFile(file_name)
    #Model.FileWorker.addUser(file_name,user)
    users = Model.FileWorker.getAllUser(file_name)
    tt = AlertTime.TimeWorker()
    #tt.NamozCames(0)
    rest = Web.WebWorker(url,data)
    response = rest.sendData()
    resData = response.json()
    current = resData["data"][now.day - 1]
    times = current['timings']

    vaqt.set(times['Fajr'].split(" ")[0] ,times['Sunrise'].split(" ")[0],times['Dhuhr'].split(" ")[0],
             times['Asr'].split(" ")[0],times['Maghrib'].split(" ")[0],times['Isha'].split(" ")[0])
    print(vaqt.getAll())
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    #dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('vaqt',todayTimes))
    print("Begin")
    updater.start_polling()
    updater.idle()
    bot = telegram.Bot(TOKEN)


if __name__ == "__main__":
    main()
