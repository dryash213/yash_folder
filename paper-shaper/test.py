def magic_num(n):
    sum = 0 
    while n>0:
        if n==0:
            n=sum 
        reminder= n%10
        print(reminder,"Remainder")
        sum+= reminder
        print(sum,"SUM")
        n=n//10
        print(n,"N ki value")
    if(n==1):
        return True
    else:
        return False

print(magic_num(123))