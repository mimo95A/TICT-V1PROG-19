def convert(c):
    f=(c*1.8)+32
    return f
print(convert(25))
def table(c):
    for c in range (-30,41,10):
        f=convert(c)
        print('{:5} {:10}'.format(convert(c),c))
    return f
print(table(-30))









