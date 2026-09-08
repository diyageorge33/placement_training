dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
n=input()
list1=[""]
for i in n:
    newlst=[]
    for x in dict[int(i)]:
        for y in list1:
            newlst.append(y+x)
    list1=newlst
print(*list1)
