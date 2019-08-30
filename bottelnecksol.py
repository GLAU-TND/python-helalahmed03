n=int(input("enter the no of bottles"))
res=list(map(int,input().split(' ')))

print(max([res.count(i) for i in res]))



