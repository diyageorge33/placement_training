n1=int(input())
n2=int(input())
list1=[int(input())for i in range(n1)]
list2=[int(input())for i in range(n2)]
new=list1+list2
new.sort()
newset=set(new)
a=list(newset)

l=len(a)
if l%2==0:
    m=(a[l//2]+a[(l//2)-1])/2
else:
    m=a[l//2]
print(m)

