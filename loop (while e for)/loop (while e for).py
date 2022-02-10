minha_variavel='ola mundo'
print(len(minha_variavel))
print(minha_variavel[0])
print(minha_variavel[1])
print(minha_variavel[2])
#for ->para
for letra in minha_variavel:
    print(letra)
lista=[0,1,2,3,4,5,6,7,8,9,10]
print(lista)
#range(start,stop,step)
#start=0
#step=1
li=range(10)
print(li)
print(list(range(11)))
print(set(range(11)))
print(tuple(range(11)))
print(list(range(1,12,2)))
numero_pares=list(range(0,11,2))
print(numero_pares)
for numero in numero_pares:
    print(numero**3)
#while->enquanto
x=0
while x <=10:
    print(x**3)
    x=x+2#imcrementar
usuario_quiser=True
while usuario_quiser==True:
    usuario_input=input("Quer continuar? (S/N)")
    if usuario_input=='N':
        usuario_input=False

