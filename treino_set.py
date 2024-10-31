
escolhidos = set()
for i in range(5):
    nome = input("Digite o nome:")
    escolhidos.add(nome)
    print(escolhidos)

    #ou

escolhidos = {"Maria, Madalena, Carina, Hadine"}
print(escolhidos)

# uniao

{1, 3, 4}.union({1,2,4}) 
{1,3}.union ({2, 4})


#interseçao

s.intersection(t)

{1, 3, 4}.intersection({1,2,4}) = {1, 4}

#difference 

s.difference(t)

{1, 3, 4}.difference({1, 2, 4}) = {3}

#pertinencia, 'in'

3 in {1,2,3,4} = True
5 in {1,2,3,4} = False
1 in {} = False


