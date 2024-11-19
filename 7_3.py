studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]
srows = [sum(x) for x in studentencijfers]


def gemiddelde_per_student(studentencijfers):
    i = 0
    gemiddelde1 = []
    for i in range(len(studentencijfers)):
        gemiddelde1.append(srows[i] / 3)
        i = i + 1
    return gemiddelde1

def gemiddelde_van_alle_studenten(studentencijfers):
    x = 0
    i = 0
    for i in range(len(studentencijfers)):
        x = (srows[i] + x)
        i = i + 1
    return x // 4

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))


