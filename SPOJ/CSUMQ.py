from itertools import accumulate
n=int(input())
a=list(map(int,input().rstrip().split()))
b=list(accumulate(a))
q=int(input())
for i in range(q):
    l,r=list(map(int,input().split()))
    if l==r:
        print(a[l])
    else:
        print(b[r]-b[l]+a[l])
