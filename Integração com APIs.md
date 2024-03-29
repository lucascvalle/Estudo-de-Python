### Neste módulo vamos entender o que são APIs e como integrar o Python com este recurso.
### API: É um conjunto de códigos para usar um serviço/site/aplicativo específico. Cada site/ferramenta tem sua própria API. É importante que você saiba ler as APIs que precisar para saber usar
#### O processo funciona da seguinte forma: O código faz uma requisição para a API e a API retorna uma resposta. 
#### Um dos padrões mais comuns em API é pegar informações em formato json, uma espécie de dicionário que precisa ser tratada no Python para podermos analisar
#### Dentro do Python existe uma biblioteca chamada Requests
#### As possibilidades de API são infinitas, vamos fazer 2 exemplos aqui: Cotação de Moedas e Envio de SMS.
#### O que precisamos?
#### Quase sempre você precisa de uma conta para consumir uma API. Algumas APIs são abertas, como a https://docs.awesomeapi.com.br/api-de-moedas , mas em muitos casos (como veremos no caso do SMS) vamos precisar ter uma conta ativa para consumir a API
#### A Documentação da API (ou exemplos da internet) é a chave para conseguir usar uma API

#### Vamos começar pegando as cotações atual de todas as Moedas
#### Para isso iremos precisar de duas bibliotecas.
````
import requests # Para fazer uma requisição
import json # A ideia é converter a informação do formato JSON para um dicionário em Python.

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all') # O Site disponibiliza o link que fornece a cotação de todas as moedas.
cotacoes_dic = cotacoes.json()
print(cotacoes_dic)

# Qual foi a última cotação do Dólar, do Euro e do BitCoin?
print('Dólar: {}'.format(cotacoes_dic['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic['EUR']['bid']))
print('Bitcoin: {}'.format(cotacoes_dic['BTC']['bid']))

# Pegar a cotação dos últimos 30 dias do dólar
cotacoes_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dolar_dic = cotacoes_dolar30d.json()
lista_cotacoes_dolar = [float(item['bid']) for item in cotacoes_dolar_dic]
print(lista_cotacoes_dolar)

# Pegar as cotações do BitCoin de Jan/20 a Out/20
cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20200101&end_date=20201031')
cotacoes_btc_dic = cotacoes_btc.json()
lista_cotacoes_btc = [float(item['bid']) for item in cotacoes_btc_dic]
lista_cotacoes_btc.reverse()
print(lista_cotacoes_btc)
print(len(lista_cotacoes_btc))

# Gráfico com as cotações do BitCoin

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc)
plt.show()
````

### Agora vamos utilizar uma API que é necessário ter o Login para realizar a tarefa.
#### O 1º Passo de toda API com Login é criar uma conta e pegar suas credenciais
#### No seu código, o 1º passo é sempre estabelecer a conexão com a API, usando seu login e suas credenciais
#### Crie uma conta neste website: https://www.twilio.com/docs/libraries/python
#### Instale no prompt do seu editor o "pip install twilio"
#### Após criar o cadastro vamos pegar o SID e o Token.
````
from twilio.rest import Client

account_sid = 'suachavesid"
token = 'seutoken"
````
#### De acordo com as regras é necessário gerar um número para enviar e verificar um número para receber as mensagens.
#### Iremos procurar o recurso "Get a Twilio Number"
````
remetente = '+15673343563'
destino = 'seunumero'

client = Client(account_sid, token) # Identificamos o usuário

# Agora iremos definir a mensagem identificado o usuário, definindo a mensagem, dizendo quem irá enviar (remetente) e quem irá receber (destino)
message = client.messages \
                .create(
                     body="Hello, World",
                     from_=remetente,
                     to=destino
                 )
print(message.sid)
````
### Criação de REST API
#### REST nada mais é que uma forma de dois sistemas computacionais de se comunicarem utilizando da tecnologia HTTP usada pelos web browsers e servidores.
#### Utilizaremos essa base de dados: https://docs.google.com/spreadsheets/d/1-m7Ba4U582rPHradwKLnMBbcoWPeIMIy/edit?usp=share_link&ouid=106510620305921502117&rtpof=true&sd=true
#### E como isso funciona?
#### A API utiliza os protocolos web GET (Pegar informação), POST (Criar Informação), PUT/PATCH (Atualizar Informação) e DELETE (Apagar informação) para trabalhar as informações.
#### Aqui iremos aprender a construir uma API, para isso utilizaremos Flask que é um Framework do Python.
#### Vamos começar:
````
from flask import Flask
import pandas as pd

app = Flask(__name__) # Cria o site
tabela = pd.read_excel("Vendas - Dez.xlsx")

# Retornando o faturamento total.
@app.route("/") # Decorator -> Diz em qual link/página a função vai rodar
def fat(): # Função -> Define o que vai acontecer na página
    faturamento = float(tabela["Valor Final"].sum())
    return {"faturamento": faturamento} # Fazendo com que o retorno da função seja um dicionário Python, podemos considerar que o retorno é um JSON, definindo assim como parte de uma API

# Vendas de todos os produtos
@app.route("/vendas/produtos") 
def vendas_produtos(): 
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

# Vendas de um produto específico
# Neste caso basta apenas passar o nome do produto exatamente como está na tabela
@app.route("/vendas/produtos/<produto>") 
def fat_produto(produto): 
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    else:
        return {produto: "Inexistente"}
    
app.run() # coloca o site no ar
````
#### Podemos usar alguns sites/ferramentas para disponibilizar a API em links online, um exemplo é o Replit (https://replit.com/) que fornece esse serviço para teste de forma gratuita ou pago para mantê-lo online 24h.
#### Neste caso em especial apenas é necessário mudar a ultima linha onde há app.run() por: app.run('host=0.0.0.0')

### Introdução a Firebase e armazenando informações Online
#### O Firebase é um conjunto de serviços online que oferece um serviço de hospedagem de informações de forma não relacional (NoSQL), com a estrutura de árvore.
#### Criando um projeto no console do Firebase vamos fazer a integração com o Python.
#### Em "Criação" iremos para "Realtime Database" e "Criar banco de dados", configurando a criação do banco de dados baseado no melhor para você de acordo com a localização:
#### Nas regras do Banco de dados vamos iniciar em modo de teste.
#### Na construção do Banco de dados começamos adicionando chaves e valores. Caso seja passado apenas a Chave sem o valor, criamos uma pasta.

#### Sendo assim no banco de dados iremos criar da seguinte forma:
 /Vendas/ID1/{cliente: "fulano", }
 /Produtos/PiD1/{nome: "fone de ouvido", quantidade: 200, preco: 100}

#### Agora que criamos uma estrutura básica para o nosso banco de dados podemos perceber que o banco de dados possui um Link (onde adicionamos a primeira "pasta")
#### Sendo assim agora iremos fazer a integração do Python com a REST API do Firebase através desse link.
#### Vamos começar importando as duas bibliotecas que já fizemos antes:
````
import requests
import json

link = "seu_link_aqui"
````
### Criar um novo produto (POST)
#### Começamos criando um dicionário de Python com as informações que vamos criar utilizando uma variável que represente os dados:
````
dados = {'nome': 'teclado', 'preco': 150, 'quantidade': 80}
requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados)) 
````
#### Repare que para evitar mudar o link da variável vamos usar o f-string para adicionar o endereço "/Produtos" e editar diretamente na pasta de produtos e terminar com "/.json".
#### Além disso precisamos passar o dicionário que criamos junto com o método json.dumps()
````
print(requisicao) # Para verificarmos se a requisição foi feita com sucesso iremos esperar que o código retorne o código 200 
print(requisicao.text) # Ele irá retornar um ID aleatório para o produto.

````

### Criar uma venda (POST)
````
dados = {'cliente': 'alon', 'preco': 150, 'produto': 'teclado'}
requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)
````
#### Rode o mesmo código novamente e veja que será gerado um novo ID para uma nova venda, mesmo que os dados sejam os mesmos.

### Editar a venda (PATCH)
````
dados = {'cliente': 'fulano'} # Vamos mudar que a venda feita anteriormente para o "Alon" foi na verdade feita para o "Fulano"
requisicao = requests.patch(f'{link}/Vendas/-NQ-zGUJ0bytjIV1zYfw/.json', data=json.dumps(dados)) # Vamos passar o ID único que foi criado na venda.
print(requisicao)
print(requisicao.text)
````
#### As informações que não foram passadas no dicionário não será alteradas ou removidas, uma vez que o código entende que deve apenas atualizar as informações mencionadas.

### Pegar uma venda específico ou todas as vendas (GET)
````
requisicao = requests.get(f'{link}/Vendas/.json') 
print(requisicao) # Primeiro pegamos todas as informações do banco de dados:
dic_requisicao = requisicao.json()
print(dic_requisicao) # Aqui podemos visualizar que as vendas foram armazenadas no dicionário.
````
#### Como queremos descobrir o ID de uma venda sem precisar visualizar manualmente, vamos percorrer o nosso dicionário
````
id_alon = None # Onde será atribuido o ID do cliente
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == "alon":
        print(id_venda)
        id_alon = id_venda # Ao final atribuimos o ID identificado pelo Loop à variável que criamos anteriormente.
````
### Deletar uma venda (DELETE)
````
requisicao = requests.delete(f'{link}/Vendas/{id_alon}/.json')
print(requisicao)
print(requisicao.text)
````
