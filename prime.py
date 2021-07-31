def prime(n):
    t=0
    if n==2:
        t=1
    else:
        for i in range(3,n):
            if n%i==0:
                t=0
            else:
                t=1
    if t==1:
        print(n,"is prime")
    else:
        print(n,"is not prime")
                



n=int(input())
prime(n)
