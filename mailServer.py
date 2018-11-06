class MailServer:
    def __init__(self):
        self.items = []

    def post(self, item):
        self.items.append(item)

    def howManyMailItems(self, who):
        count = 0
        for item in self.items:
            if item.receiver == who:
                count += 1
        return count
    
    def getNextMailItem(self, who):
        foundItem = None

        for item in self.items:
            if item.receiver == who:
                foundItem = item
        
        if foundItem is None:
            pass
        else:
            self.items.remove(foundItem)
        
        return foundItem