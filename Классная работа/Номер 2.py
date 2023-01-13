a = input().split()
f = set()
for i in a:
    if i in f:
        print('YES')
    else:
        f.add(i)
        print('NO')
