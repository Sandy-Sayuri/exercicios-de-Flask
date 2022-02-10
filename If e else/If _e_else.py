#if->se
#else->senão
devo_continuar=True
if devo_continuar == True:
    print("Continue")
pessoas_conhecidas=['João','Maria','Ana','Fábio']
pessoa=input('Entre com o nome de uma pessoas:')
print(pessoa)
if pessoa in pessoas_conhecidas:
    print('Você conhece essa pessoa')

if pessoa not in pessoas_conhecidas:
    print('Você não conhece essa')

if pessoa in pessoas_conhecidas:
    print('Você conhece essa pessoa')
else:
    print('você conhece essa pessoa')



if pessoa in pessoas_conhecidas:
    print(f'Você conhece {pessoa}')
else:
    print(f'você conhece {pessoa}')
print(pessoa)
