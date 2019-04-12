import math
def prime(n):#aks algo for prime
    if n==2 or n==3:
        return(1)
    if n%2==0 or n%3==0 or n==1:
        return(0)
    w=2
    p=math.sqrt(n)
    for l in range(5,int(p)+1,w):
        if n%l==0:
            return(0)
        w=6-w
    return(1)
t=int(input())
for x in range(t):
    mr=raw_input().split()
    m=int(mr[0])
    r=int(mr[1])
    for n in range(m,r+1):
        if prime(n):
            print(n)
