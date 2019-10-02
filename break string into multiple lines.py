l = str(input())
z = []
c = input()
n = int(c)
for i in l:
    for j in range(l.index(i), len(l)):
        if len(i) < n and len(l[i + j]) < n:
            z.append(i)
            z.append(l[i + j])
            z.split(',')
print(l)




