import random
n=random.randint(1000,9999)
print("Welcome to cows and bulls game")
g=int(input("enter your number"))
cows=0
bulls=0
lis1=list(str(n))
lis2=list(str(g))
for i in lis2:
    if i in lis1:
        if lis2.index(i) == lis1.index(i):
            cows+=1
        else:
            bulls+=1
print("you got",cows,"cows","and",bulls,"bulls") 
