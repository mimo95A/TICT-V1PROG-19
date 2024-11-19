f= open("hardlopers.txt","w+")
import datetime
def strftime():
    i = 0
    while i < 5:
        naam = input('Voer de naam van de deelnemer in: ')
        vandaag = datetime.datetime.today()
        s = vandaag.strftime("%a %d %b %Y, %X,")
        text = s + naam + "\n"
        print(text)
        i = i+1
        f=open("hardlopers.txt","a+")
        f.write(text)
strftime()
f.close()
