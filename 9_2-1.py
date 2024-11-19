def monopolyworp():

 import random
 x=random.randrange(1,7)
 y=random.randrange(1,7)
 if x!=y:
     print(x, '+', y, '=', x + y)
 elif x==y:
    print(x, '+', y, '=', x + y, '(dubbel)')
    x = random.randrange(1, 7)
    y= random.randrange(1, 7)
    if x != y:
       print(x, '+', y, '=', x + y)
    elif x==y:
       print(x, '+', y, '=', x + y, '(dubbel)')
       x = random.randrange(1, 7)
       y = random.randrange(1, 7)
       if x != y:
         print(x, '+', y, '=', x + y)
       elif x==y :
         print(x, '+', y, '=', x + y, '(direct naar gevangenis)')
 return
(monopolyworp())





