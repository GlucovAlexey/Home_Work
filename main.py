masha = input()
if masha != "конец":
    mnmasha = {masha}
while masha != 'конец':
    masha = input()
    if masha != 'конец':
        mnmasha.add(masha)

petya = input()
if petya != "конец":
    mnpetya = {petya}
while petya != 'конец':
    petya = input()
    if petya != 'конец':
        mnpetya.add(petya)

ans = mnpetya.intersection(mnmasha)
for i in ans:
    print(i)
