from messages import Message
from time import time
from email.message import EmailMessage
import smtplib

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

def Email(bot):
    bot.Time = time()
    emailID = 'anonymousstark1@gmail.com'
    passWd = 'nonewsisgoodnews'
    msg = bot.Message[7:]

    emailMsg = EmailMessage()
    emailMsg.set_content(msg)
    emailMsg['Subject'] = 'Message Sent by Bot [no-reply]'
    emailMsg['To'] = bot.email
    emailMsg['From'] = emailID

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailID, passWd)
    server.send_message(emailMsg)
    server.quit()
    bot.sendMessage('Mail was sent', bot.ThID, bot.ThType)
    bot.Time = time()
