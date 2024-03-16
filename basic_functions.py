def user_methods(inObj):
    for items in dir(inObj):
        if items[0] != "_":
            print(items)
