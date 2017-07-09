from commands import *
from time import time

Commands = {
        '.Start': (Start, 'A'),
        '.Stop': (Stop, 'A'),
        '.Exit': (Exit, 'A'),
        }


def executeCommand(bot):
    try:
        if Commands[bot.Message][1] == 'A' and bot.uid != bot.AID:
            raise KeyError
        Commands[bot.Message][0](bot)
    except KeyError as e:
        if bot.uid == bot.AID:
            if bot.Message not in Commands and time() - bot.Time < 20:
                return None
            bot.Time = time()
            bot.sendMessage('Sorry, Master that command was unknown, following commands are known', bot.ThID, bot.ThType)
            for key in Commands:
                if 'A' in Commands[key][1]:
                    bot.sendMessage('<dot>' + key, bot.ThID, bot.ThType)
        else:
            bot.Time = time()
            buildIn_Unavailable(bot)
            for key in Commands:
                if 'U' in Commands[key][1]:
                    bot.sendMessage(key, bot.ThID, bot.ThType)
