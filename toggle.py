n=int(input())
n=bin(n)
new=n[2:]
print(new)
b=new.replace("0","x")
c=b.replace("1","0")
d=c.replace("x","1")
print(int(d,2))

