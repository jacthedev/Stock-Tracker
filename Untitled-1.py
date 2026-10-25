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
def total_units(stock):
    total = 0
    for amount in stock.values():
        total += amount
    return total

def total_units(stock):
    total = 0
    for amount in stock.values():
        total += amount
    return total

def total_units(stock):
    total = 0
    for amount in stock.values():
        total+=amount
    return total
       # 5
def most_stocked(stock):
  best_name=None
  best_amount=None
  for name, amount in stock.items():
   if best_amount ==None or amount > best_amount:
    best_amount = amount
    best_name = name
  return best_name

def sorted_by_amount(stock):
  remaining=dict(stock)
  result = []
  while len(remaining)>0:
    smallest_name = None
    smallest_amount = None
    for name, amount in remaining.items():
      if smallest_amount is None or amount < smallest_amount:
        smallest_amount = amount
        smallest_name = name
    del remaining[smallest_name]
    result.append(smallest_name)
  return result
add_stock(stock, "kiwi", 3)
add_stock(stock, "mango", 5)
remove_stock(stock, "yam", 10)
remove_stock(stock, "mango", 2)
report(stock, 5)
print(low_items(stock, 5))



