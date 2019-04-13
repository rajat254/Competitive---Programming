#simple dfs
from sys import stdin
from collections import defaultdict as df
def dfs(visited,t):
    visited[t]=True
    for i in d[t]:
        if visited[i]==False:
            dfs(visited,i)
        else:
            return 0
    return 1
n,m=list(map(int,stdin.readline().split()))
d=df(list)
for x in range(m):
    a,b=list(map(int,stdin.readline().split()))
    d[a].append(b)
visited=[0]*(n+1)
result=dfs(visited,1)
visited.pop(0)
if n==m+1 and result==1:
    if False in visited:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
