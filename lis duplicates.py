lis=list(map(int,input().split()))
lis1=[]
for i in lis:
    if i not in lis1:
        lis1.append(i)
print(lis1)
