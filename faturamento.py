#importando bibliotecas uteis
import pandas as pd
import json

#usando contexto para ler o json e transferir os valores para uma variavel
with open('dados.json') as registro:
    dados = json.load(registro)

#criando um dataframe pandas a partir da variavel dados
df = pd.DataFrame(dados)

#excluindo valores zerados de faturamento da base de dados
df = df[df["valor"] != 0]

#visualizando base de dados tratada
print(df)

#mostrando menor valor
print("\nO menor valor de faturamento mensal foi: R$", df["valor"].min())

#mostrando maior valor
print("\nO maior valor de faturamento mensal foi: R$", df["valor"].max())

#calculando media mensal
media_mensal = df["valor"].mean()

#contando valores acima da media mensal
contador = (df["valor"] > media_mensal).sum()

#mostrando resultado
print("\nO numero de dias com faturamento acima da media mensal foi", contador)




