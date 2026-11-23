class Shelf:
    def __init__(self):
        self.items = {}

    def add(self, item, amount):
        self.items[item] = self.items.get(item, 0) + amount
        self.history.append((item,amount))

    def remove(self, item, amount):
        left = self.items.get(item, 0) - amount
        if left < 0:
            self.items[item] = 0
        else:
            self.items[item] = left
    def report(self, limit):
        for item, amount in self.items.items():
            if amount < limit:
                print(item, amount, "low")
            else:
                print(item,amount)
    def low(self, limit):
        low = []
        for item,amount in self.items.items():
            if amount < limit:
                low.append(item)
        return low
    
    def undo(self):
     record = self.history.pop()
     self.items[record[0]] -= record[1]

    def summary(self):
     print(self.name, ":"len(self.shelf.items)"items")

    def restock(self,item,amount):
        self.shelf.add(item,amount)

    def sell(self,item,amount):
     self.shelf.remove(item,amount)

    def low_names(self,limit):
     return self.shelf.low(limit)

    def total(self):
     result = 0
     for amount in self.items.values():
      result+=amount
        return result