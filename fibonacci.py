def fibonacci(n):
    a=0
    b=1
    c=0
    if(n==1):
        print("fibonacci series is:")
        print(a)
    else:
        while(c<n):
            print(a)
            t= a+b
            a=b
            b=t
            c+=1
    print(a,b)


n=int(input())
if n<0:
    print("enter valid number")
print(fibonacci(n))
