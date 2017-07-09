from messages import Message
from time import time

def Start(bot):
    bot.Time = time()
    if bot.userOnline == True:
        bot.userOnline = False
        bot.sendMessage(Message['Start'], bot.ThID, bot.ThType)
    else:
        bot.sendMessage(Message['AlreadyStarted'], bot.ThID, bot.ThType)

def Stop(bot):
    bot.Time = time()
    if bot.userOnline == False:
        bot.userOnline = True
        bot.sendMessage(Message['Stop'], bot.ThID, bot.ThType)
    else:
        bot.sendMessage(Message['AlreadyStopped'], bot.ThID, bot.ThType)

def buildIn_Unavailable(bot):
    bot.sendMessage(Message['Unavailable'], bot.ThID, bot.ThType)

def Exit(bot):
    bot.Time = time()
    bot.sendMessage(Message['Exit'], bot.ThID, bot.ThType)
    bot.stopListening()
