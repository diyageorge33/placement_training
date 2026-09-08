def strongpassword(pw):
    upper=False
    lower=False
    digit=False
    
    for i in pw:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit=True

    count=0
    count2=0
    count3=0
    if not upper:
        count=count+1
    if not lower:
        count=count+1
    if not digit:
        count=count+1

    if(len(pw)<6):
            count2=6-len(pw)

    for i in range(1,len(pw)-1):
        if pw[i-1]==pw[i]==pw[i+1]:
            count3=count3+1
    return max(count,count2,count3)
    
password=input()
x=strongpassword(password)
print(x)