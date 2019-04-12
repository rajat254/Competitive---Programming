# your code goes here
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().rstrip().split()))
    index=-1# initialise index as -1
    for i in range(n-1,-1,-1):
        if a[i]>a[i-1]:
            index=i-1
            break
    if index==-1:#if permutation is maximum i.e no larger permutations can be made
        print(-1)
    else:
        for i in range(n-1,index,-1):
            if a[index]<a[i]:
                a[index],a[i]=a[i],a[index]
                break
        a=a[0:index+1]+list(reversed(a[index+1:]))
        print(''.join(str(e) for e in a))
