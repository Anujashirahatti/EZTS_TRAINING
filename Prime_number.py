n=int(input())
count=0
for i in range(2,n+1):
    p=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            p=False
    if p:
        count=count+1
print(count)