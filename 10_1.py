try:
    Aantal = int(input('het aantal personen '))
    if Aantal<0:
        print('Negatieve getallen zijn niet toegestaan')
    else:
     y = 4356 / Aantal
     print(y)
except ZeroDivisionError:
     print ('Aantal', Aantal,' Delen door nul kan niet' )
except ValueError:
    print( 'Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer')
