n=int(input())
arr=list(map(int,input().split()))
s=int(input())
new=[]
for i in arr:
    x=bin(i)
    x=x[2:]
    x=x[:-s]
    if x=="":
        new.append(0)
    else:
        new.append(int(x,2))
print(*new)
