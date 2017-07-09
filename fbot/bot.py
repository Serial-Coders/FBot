from fbchat import Client
from fbchat  import log
from executor import executeCommand
import logging

class Bot(Client):
    def __init__(self, email, pswd, usr=None, mx=5, ssn=None, log=logging.INFO):
        super(Bot, self).__init__(email, pswd, usr, mx, ssn, log)
        self.userOnline = False
        self.AID = None
        self.Message = None
        self.ThID = None
        self.ThType = None
        self.Time = 0

    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        self.AID = author_id
        self.Message = message
        self.ThID = thread_id
        self.ThType = thread_type

        executeCommand(self)

