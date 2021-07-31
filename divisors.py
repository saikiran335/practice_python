n=int(input())
lis=[]
for i in range(1,100):
    if n%i==0:
        lis.append(i)
print(lis)
