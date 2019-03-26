from collections import defaultdict as df
n=int(input())
d=df(list)
for i in range(n-1):
    a,b=list(map(int,input().split()))
    d[a].append(b)
    d[b].append(a)
visited=[False]*(n+1)
dp=[0]*(n+1)
s=[]
s.append(1)
while(len(s)>0):
    f=s.pop(0)
    for j in d[f]:
        if visited[j]==False:
            visited[j]=True
            s.append(j)
            dp[j]=dp[f]+1
index=dp.index(max(dp))
s=[]
dp=[0]*(n+1)
s.append(index)
visited=[False]*(n+1)
while(len(s)>0):
    f=s.pop(0)
    for j in d[f]:
        if visited[j]==False:
            visited[j]=True
            s.append(j)
            dp[j]=dp[f]+1
print(max(dp))
