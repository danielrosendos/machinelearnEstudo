from sklearn.naive_bayes import MultinomialNB

#[É gordo, tem pernas curtas?, faz auau?]
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]

cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1,porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacao = [1,1,1,-1,-1,-1]

misterioso = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]

teste = [misterioso, misterioso2,misterioso3]

misterioso_teste = [-1,1,-1]

modelo = MultinomialNB()
modelo.fit(dados, marcacao)
resultado = modelo.predict(teste)

diferencas = resultado - misterioso_teste

acerto = [d for d in diferencas if d == 0]

total_de_acerto = len(acerto)

total_de_elemento = len(teste)

print(resultado)
print(total_de_acerto-total_de_elemento)
print(100*total_de_acerto/total_de_elemento,"%")
