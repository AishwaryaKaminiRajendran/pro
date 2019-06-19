n,q=map(int,input().split())
y=[]
b=[]
d=0
c=0
a=[int(n) for n in input().split() ]
for i in range(0,q):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        b.append(a[j])
    x=sum(b)
    y.append(x)
print(y[0])
for z in range(1,len(y)):
    print(y[z]- y[z- 1])
        
        
        
        
        
        
