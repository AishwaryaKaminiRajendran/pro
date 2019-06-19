
n,q=map(int,input().split())
y=[]
b=[]
d=0
c=0
a=[int(n) for n in input().split() ]
#print(a)
for i in range(0,q):
    u,v=map(int,input().split())
#    print(u,v)

    for j in range(u,v+1):
        b.append(a[j])
 #   print(b)
    x=sum(b)
 #   print(x)
    y.append(x)
#print(y)
print(y[0])
for z in range(1,len(y)):
    print(y[z]- y[z- 1])
        
        
        
        
        
        
