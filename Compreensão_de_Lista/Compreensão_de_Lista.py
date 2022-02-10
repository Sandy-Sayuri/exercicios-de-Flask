for x in range(5):
    print(x)
print(list(range(0,10,2)))
print(10%3)#resto
print(1%2)
print([n for n in range(11)if n %2==0])
pessoas=['Ana','Manuela','Felipe','Pedro']
ana='Ana'
print(ana.strip())#retira espaços
print(ana.upper())
print(ana.lower())
print(ana.strip().capitalize())
print(pessoas)
pessoas_normalizadas=[pessoa.strip().capitalize()for pessoa in pessoas]
print(pessoas_normalizadas)