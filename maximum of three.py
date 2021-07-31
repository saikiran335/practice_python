def maximum(a,b,c):
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print("c is greater")
a,b,c=input().split()
maximum(a,b,c)
