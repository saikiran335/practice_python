import random
print("welcome to guessing game || I WILL GUESS YOU")
n=int(input())
c="no"
count=1
while c=="no":
    g=random.randint(1,10)
    if g!=n:
        c="no"
        print(g)
        count+=1
        
    elif g==n:
        c="yes"
        print(g)
print(count,"guesses")
