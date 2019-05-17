from collections import defaultdict as df
from sys import stdin , stdout
from collections import deque
while(1):
    a,b=list(map(int,stdin.readline().split()))
    a,b=b,a
    if a==b==0:
        exit()
    else:
        arr=[[0]*b for i in range(a)]
        for i in range(a):
            s=input().rstrip()
            for j in range(b):
                if s[j]=='S':
                    r1,c1=i,j
                    continue
                if s[j]=='D':
                    r2,c2=i,j
                    continue
                if s[j]=='X':
                    arr[i][j]='X'
                else:
                    arr[i][j]=int(s[j])
        pika=input().rstrip()
        dis=[[float('inf')]*b for i in range(a)]
        s=[]
        dis[r1][c1]=0
        s=deque()
        s.append((r1,c1))
        arr[r1][c1]=0
        arr[r2][c2]=float('inf')
        while(len(s)>0):
            f=s.popleft()
            x1,y1=f[0],f[1]
            if x1+1<a:
                if arr[x1+1][y1]!='X':
                    if dis[x1+1][y1]>dis[x1][y1]+arr[x1+1][y1]:
                        dis[x1+1][y1]=dis[x1][y1]+arr[x1+1][y1]
                        s.append((x1+1,y1))
            if x1-1>=0:
                if  arr[x1-1][y1]!='X':
                    if dis[x1-1][y1]>dis[x1][y1]+arr[x1-1][y1]:
                        dis[x1-1][y1]=dis[x1][y1]+arr[x1-1][y1]
                        s.append((x1-1,y1))
            if y1+1<b:
                if arr[x1][y1+1]!='X':
                    if dis[x1][y1+1]>dis[x1][y1]+arr[x1][y1+1]:
                        dis[x1][y1+1]=dis[x1][y1]+arr[x1][y1+1]
                        s.append((x1,y1+1))
            if y1-1>=0:
                if arr[x1][y1-1]!='X':
                    if dis[x1][y1-1]>dis[x1][y1]+arr[x1][y1-1]:
                        dis[x1][y1-1]=dis[x1][y1]+arr[x1][y1-1]
                        s.append((x1,y1-1))
        mini=float('inf')
        if r2+1<a:
            mini=min(mini,dis[r2+1][c2])
        if r2-1>=0:
            mini=min(mini,dis[r2-1][c2])
        if c2-1>=0:
            mini=min(mini,dis[r2][c2-1])
        if c2+1<b:
            mini=min(mini,dis[r2][c2+1])
        print(min(mini,dis[r2][c2]))
