def new_password(new,old):
    if new!=old and len( new)>=6:
        return True
    else:
        return False
print(new_password('126','3456'))
