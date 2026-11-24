from shelf import Shelf

# test 1: add works
shelf = Shelf()
shelf.add("kiwi", 3)
assert shelf.items == {"kiwi": 3}

# test 2: remove can't go negative
shelf = Shelf()
shelf.add("kiwi", 3)
shelf.remove("kiwi", 10)
assert shelf.items == {"kiwi": 0}

# test 3: add refuses zero
shelf = Shelf()
try:
    shelf.add("kiwi", 0)
    assert False, "add should have refused an amount of 0"
except ValueError:
    pass

print("all tests passed")