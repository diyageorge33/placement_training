def checkpassword(str,n):
    digit=False
    capital=False
    if n<4:
        return 0
    if str[0].isdigit():
        return 0
    
    for i in str:
        if i.isdigit():
            digit=True
        if i.isupper():
            capital=True
        if (i==" " or i=="/"):
            return 0
    if digit and capital:
        return 1


inp=input()
n=len(inp)
x=checkpassword(inp,n)
print(x)