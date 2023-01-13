a = int(input('Введите кол-во учеников.'))
s = set()
for x in range(a):
    y = int(input('Введите кол-во языков, которые знает ученик.'))
    for w in range(y):
        r = input()
        s.add(r)


print(len(s))
print(s)
