import math
d=input()
leng=0
x1=0
y1=0
z1=0
if d=='3D':
    x=int(input())
    y=int(input())
    z=int(input())
    const=int(input())
    alpha=int(input())
    axis=input()
    alpha=math.radians(alpha)
    leng=(x**2+y**2+z**2)**0.5
    x*=const
    y*=const
    z*=const
    if axis=='X':
        x1=x
        y1=y*math.cos(alpha)-z*math.sin(alpha)
        z1=y*math.sin(alpha)+z*math.cos(alpha)
    elif axis=='Y':
        x1=x*math.cos(alpha)+z*math.sin(alpha)
        y1=y
        z1=z*math.cos(alpha)-x*math.sin(alpha)
    else:
        x1=x*math.cos(alpha)-y*math.sin(alpha)
        y1=x*math.sin(alpha)+y*math.cos(alpha)
        z1=z
    print('lengh:',leng,',scaled coordinates:',x,',',y,',',z,', rotated coordinates:',x1,',',y1,',',z1)
elif d=='2D':
    x=int(input())
    y=int(input())
    const=int(input())
    alpha=int(input())
    alpha=math.radians(alpha)
    leng=(x**2+y**2)**0.5
    x*=const
    y*=const
    x1=x*math.cos(alpha)-y*math.sin(alpha)
    y1=x*math.sin(alpha)+y*math.cos(alpha)
    print('lengh:',leng,',scaled coordinates:',x,',',y,'rotated coordinates:',x1,',',y1)