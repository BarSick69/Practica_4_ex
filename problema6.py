import math


def can_be_triangle(x,y,z):
    if(x+y>z and y+z>x and z+x>y):
        return True
    else:
        return False
def perimetru(x,y,z):
    return x+y+z
def aria(x,y,z):
    semi=perimetru(x,y,z)/2
    return round(math.sqrt(semi*(semi-x)*(semi-y)*(semi-z)),2)
latura=[]
A=int(input("dati a: "))
latura.append(A)
B=int(input("dati b: "))
latura.append(B)
C=int(input("dati c: "))
latura.append(C)
D=int(input("dati d: "))
latura.append(D)
for i in range(0,len(latura)):
    for j in range(0,len(latura)):
        for k in range(0,len(latura)):
            if(i!=j and j!=k and k!=i):
                a=latura[i]
                b=latura[j]
                c=latura[k]
                if(can_be_triangle(a,b,c)):
                    print("Numerele:",a," ",b," ",c," pot forma un triunghi")
                    print("Perimetrul triunghiului cu laturele:",a," ",b," ",c," este:",perimetru(a,b,c))
                    print("Aria triunghiului cu laturele:",a," ",b," ",c," este:",aria(a,b,c))
                else:
                    print("Numerele:",a," ",b," ",c," nu pot forma un triunghi")
            