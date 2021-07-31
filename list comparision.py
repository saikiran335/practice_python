lis1=list(map(int,input().split()))
lis2=list(map(int,input().split()))
lis3=[]
for i in lis1:
    for j in lis2:
        if i in lis2:
            if i not in lis3:
                lis3.append(i)
        if j in lis1:
            if j not in lis3:
                lis3.append(j)

print(lis3)
