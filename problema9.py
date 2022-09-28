import math
def inaltimea_trg(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp=(a+b+c)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-c)),3)
        ha=round((2*aria)/a,3)
        hb=round((2*aria)/b,3)
        hc=round((2*aria)/c,3)
        return print("Inaltimea triunghiului pe latura cu lungimea",a,"are lungimea:",ha,"\nPe latura cu lungimea",b,"are lungimea",hb,"\nPe latura cu lungimea",c,"are lungimea",hc)
    else:
        return print("Laturile date nu pot forma un triunghi!")


o=int(input("Dati I-ul nr: "))
p=int(input("Dati II-a nr: "))
r=int(input("Dati III-a nr: "))  

(inaltimea_trg(o,p,r))