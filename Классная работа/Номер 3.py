k = int(input())
m = set()
for x in range(k):
    t = set(input().split())
    m.update(t)
    # for i in input().split():
    # m.add(i)
print(len(m))


