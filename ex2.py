lista_numerelor=[]
def max(a,b):
    if a>b:
        return a
    else:
        return b
def min(a,b):
    if a<b:
        return a
    else:
        return b
for i in range(0,8):
    numar=float(input("Dati numarul {}:".format(i+1)))
    lista_numerelor.append(numar)
print(lista_numerelor)
suma=max(min(lista_numerelor[0],lista_numerelor[1]),max(lista_numerelor[2],lista_numerelor[3]))+min(max(lista_numerelor[4],lista_numerelor[5]),min(lista_numerelor[6],lista_numerelor[7]))
print("a)",suma)
lista_numerelor=[]
for i in range(0,10):
    numar=float(input("Dati numarul {}:".format(i+1)))
    lista_numerelor.append(numar)
print(lista_numerelor)
t=min(lista_numerelor[0],lista_numerelor[1])+min(lista_numerelor[2],lista_numerelor[3])+min(lista_numerelor[4],lista_numerelor[5])+min(lista_numerelor[6],lista_numerelor[7])+min(lista_numerelor[8],lista_numerelor[9])
t+=max(lista_numerelor[0],lista_numerelor[1])+max(lista_numerelor[2],lista_numerelor[3])+max(lista_numerelor[4],lista_numerelor[5])+max(lista_numerelor[6],lista_numerelor[7])+max(lista_numerelor[8],lista_numerelor[9])
print("b)",t)