l = list(map(int, input().split()))
s = l
c = 0
d = sorted(l, reverse=True)
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if l[i] >= l[j]:
            c = c + 1
c = c - 1

if c == 0 or c == 1:
    print('True')
else:
    print('False')

