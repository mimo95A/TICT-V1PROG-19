f = open("kaartnummers.txt")
for x in f:
  f1=x.split()
  print (f1[1],f1[2] ,'heeft kaartnummer: ',f1[0])
f.close()





