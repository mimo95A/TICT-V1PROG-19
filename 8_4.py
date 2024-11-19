def ticker(filename):
 return (filename.items())
print(ticker({'YAHOO':'YHOO','GOOGLE_INC':'GOOG','Harley_Davidson':'HOG', 'Yamana_Gold':'AUY','Sothebys':'BID', 'inBev':'BUD'}))


a = input('Enter Company name')
x=ticker({'YAHOO':'YHOO','GOOGLE_INC':'GOOG','Harley_Davidson':'HOG', 'Yamana_Gold':'AUY','Sothebys':'BID', 'inBev':'BUD'})
for name in x:

    if a == name[0]:
        print (name[1])
    elif a == name[1]:
        print (name[0])







