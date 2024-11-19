def namen():
    nlist = []
    name = input('Volgende naam: ')
    while name != ' ':
        nlist.append(name)
        name = input('Volgende naam: ')
    x = {}
    for name in nlist:
        if name in x:
            x[name] += 1
        else:
            x[name] = 1
    for name in x:
        if x[name] == 1:
            print('Er is ', x[name],'student met de naam', name)
        else:
            print('Er is ', x[name],'studenten met de naam', name)
namen()

