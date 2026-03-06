n=int(input())
c=0
while(n>0):
    n=n&n-1
    c=c+1
print(c)
    
