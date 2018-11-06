class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user
    
    def printNextMailItem(self):
        item = self.server.getNextMailItem(self.user)
        if item is None:
            print("No new mail.")
        else:
            item.print()
    
    def sendMailItem(self, to, msg):
        item = MailItem(self.user, to, msg)
        self.server.post(item)