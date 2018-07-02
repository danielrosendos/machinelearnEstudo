from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from collections import Counter

df = pd.read_csv('buscas2.csv')

X_df = df[['home','busca','logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

acerto_base = max(Counter(Y).values())

taxa_de_acerto_base = 100.0*acerto_base/len(Y)

print('Taxa de acerto base: %f' % taxa_de_acerto_base)

porcentagem_treino = 0.9

tamanho_treino = int(porcentagem_treino * len(Y))
tamaho_teste = len(Y) - tamanho_treino

treino_dados = X[:tamanho_treino]
treino_marcacoes = Y[:tamanho_treino]

teste_dados = X[-tamaho_teste:]
teste_marcacoes = Y[-tamaho_teste:]

modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)

resultado = modelo.predict(teste_dados)

acertos = resultado == teste_marcacoes

total_acertos = sum(acertos)
total_elementos = len(teste_dados)

taxa_acerto = 100.0*total_acertos/total_elementos

print('Taxa de acerto do algoritmo: %f' % total_acertos)
print(total_elementos)
