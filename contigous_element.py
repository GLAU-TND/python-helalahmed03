l = list(map(int, input().split()))
z = input()
n = int(z)

h = []
c = 0
s = sum(l)
if n > s:
    print('None')
else:
    for i in range(0, len(l)):
        c = l[i]
        h = []
        for j in range(i + 1, len(l)):
            h.append(l[i])
            c = c + l[j]
            h.append(l[j])
            if c == n:
                print(h)




