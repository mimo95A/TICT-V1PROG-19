try:
 naam_bestand = input('bestand naam: ')
 x = open (naam_bestand, "r")
 for inlezen in x:
  print(inlezen)
 x.close()
except:
 while True:
  print('Het bestand kan niet ingelezen worden.''\n' ' graag voer de naam van het bestand opniuwe.''\n')
  y = input('Voer het bestand naam opniuwe: ')
  if y == 'kaartnummers.txt':
   s = open(y, "r")
   for inlezen in s:
    print(inlezen)
   s.close()
   break


