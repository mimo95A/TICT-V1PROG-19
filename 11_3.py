import json

with open('inloggers.json', 'w') as f:
    data = {}

    while True:
        naam = input("Wat is je achternaam? ")
        data['naam'] = naam
        voorl = input("Wat zijn je voorletters? ")
        data['voorletters'] = voorl
        gbdatum = input("Wat is je geboortedatum? ")
        data['geb_datum'] = gbdatum
        email = input("Wat is je e-mail adres? ")
        data['email'] = email
        with open('inloggers.json', 'w') as f:
         json.dump(data, f, indent = 2)
         f.close
         break
