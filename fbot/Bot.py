from fbchat import Client
from fbchat  import log
import logging

class Bot(Client):
    def __init__(self, email, pswd, usr=None, mx=5, ssn=None, log=logging.INFO):
        super(Bot, self).__init__(email, pswd, usr, mx, ssn, log)
        self.userOnline = False
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        if author_id == self.uid:
            if message == 'Stop' and self.userOnline == False:
                self.userOnline = True
                self.sendMessage('OK done master, I know you are online', thread_id, thread_type)
            elif message == 'Start' and self.userOnline == True:
                self.userOnline = False
                self.sendMessage('Ok master, I you are going back, my work starts now', thread_id, thread_type)
        elif not self.userOnline:
            try:
                self.sendMessage("My master is not online yet, I'm \
                        his faithful bot, master will reply you back\
                        when he will be online", thread_id, thread_type)
            except:
                pass
