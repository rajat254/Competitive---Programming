import atexit,io,sys
import math
buffer=io.BytesIO()
def write():
    sys.__stdout__.write(biffer.getvalue())
t=int(input())
for x in range(t):
    arr=list(map(int,input().rstrip().split()))
    sum1=1
    n=(arr[0])
    r=n
    i=math.sqrt(n)
    i=int(math.ceil(i))
    for y in range(2,i+1):
        count=0
        if n%y==0:
            while(n%y==0):
                n=n//y
                count+=1
            sum1*=(y**(count+1)-1)//(y-1)
    count=1
    if n>1:
        sum1*=(n**(count+1)-1)//(n-1)
    print(sum1-r)
