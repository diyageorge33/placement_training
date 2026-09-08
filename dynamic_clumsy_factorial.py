inp=list(map(int,input().split()))
l=len(inp)
if l==1:
    first=inp[0]
    last=1
else:
    first=inp[0]
    last=inp[1]
list1=[]
for i in range(first,last-1,-1):
    list1.append(i)

evencount,oddcount=0,0
list2=[]
list2.append(str(list1[0]))

for i in range(1, len(list1)):
    num = list1[i - 1]
    if num % 2 == 0:
        if evencount % 2 == 0:
            o = "//"
        else:
            o = "*"
        evencount += 1
    else:
        if oddcount % 2 == 0:
            o = "+"
        else:
            o = "-"
        oddcount += 1
    list2.append(o)
    list2.append(str(list1[i]))
expression = "".join(list2)
print(eval(expression))