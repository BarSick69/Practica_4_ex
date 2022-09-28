import math
from re import X
def mediana(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        ma=round(0.5*(math.sqrt((2*(b**2))+(2*(c**2))-(a**2))),3)
        mb=round(0.5*(math.sqrt((2*(a**2))+(2*(c**2))-(b**2))),3)
        mc=round(0.5*(math.sqrt((2*(b**2))+(2*(a**2))-(c**2))),3)
        return print("Mediana laturei cu lungimea:",a, "are lungimea:",ma,"; mediana laturei cu lungimea:",b, "are lungimea",mb,"mediana laturei cu lungimea:",c, "are lungimea",mc)
    else:
        return print("Laturile date nu pot forma un triunghi!")

x=int(input("Dati latura 1: "))
y=int(input("Dati latura 2: "))
z=int(input("Dati latura 3: "))

mediana(x,y,z)
