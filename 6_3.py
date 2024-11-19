f = open("kaartnummers.txt")
max = 0
i = 0
for x in f:
    result = [x.strip() for x in x.split(',')]
    s = int (str (result[0]))
    i = i + 1
    if s > max:
        max = s
        regel = i
print('Deze file telt',i, 'regels\nHet grootste kaartnummer is:' ,max, 'en dat staat op regel',regel)





