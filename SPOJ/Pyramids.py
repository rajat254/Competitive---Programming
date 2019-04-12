import math
t=int(input())
for xi in range(t):
    U,V,w,W,v,u=list(map(int,input().split()))
    x=(U-v+w)*(v-w+U)
    y=(V-w+u)*(w-u+V)
    z=(W-u+v)*(u-v+W)
    X=(w-U+v)*(U+v+w)
    Y=(u-V+w)*(V+w+u)
    Z=(v-W+u)*(W+u+v)
    a=math.sqrt(x*Y*Z)
    b=math.sqrt(y*Z*X)
    c=math.sqrt(z*X*Y)
    d=math.sqrt(x*y*z)
    nemo=(-a+b+c+d)*(a-b+c+d)*(a+b-c+d)*(a+b+c-d)
    deno=192*u*v*w
    print(math.sqrt(nemo)/deno)
    
