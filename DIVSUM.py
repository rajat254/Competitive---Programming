from sys import stdin
t=int(stdin.readline())
for x in range(t):
    a,b=list(map(int,stdin.readline().split()))
    print(pow(a,b,10))
