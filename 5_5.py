def kwadraten_som(lst):
 totaal=0
 for int in lst:
     if int>0:
       totaal=int**2+totaal
 return totaal
print(kwadraten_som([4, 5, 3, -81]))




