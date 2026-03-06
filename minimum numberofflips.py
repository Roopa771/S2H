n=int(input())
g=int(input())
o=n^g
c=0
while(o>0):
    o=o&o-1
    c=c+1
print(c)
