stock = {"mango": 10, "yam": 4}

def add_stock(stock, item, amount):
    stock[item] = stock.get(item, 0) + amount





def remove_stock(stock, item, amount):
    left=stock.get(item, 0)-amount
    if left < 0:
        stock[item] = 0
    else :
        stock[item] = left



def low_items(stock, limit):
    low=[]
    for item, amount in stock.items():
        if amount < limit:
            low.append(item)
    return low
print(low_items(stock, 5))   

def report(stock, limit):
    for item, amount in stock.items():
        if amount < limit:
            print(item, amount, "low")
        else:
            print(item, amount)

add_stock(stock, "kiwi", 3)
add_stock(stock, "mango", 5)
remove_stock(stock, "yam", 10)
remove_stock(stock, "mango", 2)
report(stock, 5)
print(low_items(stock, 5))



