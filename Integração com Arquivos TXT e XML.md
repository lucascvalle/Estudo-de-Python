### Lendo Arquivos
##### O python possui de forma nativa métodos que podem manipular arquivos .Método open: -> Abre um arquivo txt
##### Link Arquivo txt: https://drive.google.com/file/d/1k7F2Ke9CrMSI6bZW9KKm-ZKEscTVVxHa/view

````
arquivo = open('NomeArquivo.txt', 'r')

# Usamos 'r' para abrir o arquivo para ler (read) e 'w' quando estamos abrindo o arquivo para escrever (write) ou 'a' se formos adicionar (append) uma informação no arquivotxt, não sendo necessário importar bibliotecas para isso.

arquivo_alunos = open('Alunos.txt', 'r')

# quando fazemos a definição da variável do arquivo existem 2 métodos de leitura do arquivo, o método .readlines e .read(). O método .readlines() transforma cada linha do seu texto em uma lista enquanto o .read() realiza a leitura do texto bruto tal qual apresentado no bloco .txt 

texto_arquivo = arquivo.read()

lista_linhas = arquivo.readlines()
````
### Criando arquivos
#### Utilizando o método open() com a chave 'w' (write), criamos um novo arquivo que irá substituir qualquer arquivo no mesmo local que estiver o caderno ou endereço definido
````
novo_arquivo = open('resumo.txt', 'w')
````
#### para escrever utiliza-se o método write()
````
novo_arquivo.write('Olá, Mundo!')
````
#### Apenas escrever não é o bastante para que o arquivo seja realmente modificado, sendo necessário salvar a versão mais recente do arquivo. Utilizaremos o método .close()
````
novo_arquivo.close()
````
### Método With
#### É uma estrutura que é utilizada para abrir o arquivo e ao final da estrutura já realiza o método de fechamento do arquivo.
````
with open('resumo2.txt', 'w') as arquivo2:
  arquivo2.write('Olá, mundo!\nSegunda linha')
  arquivo2.write('Terceira linha')
````   
#### Desta forma não é necessário usar o método .close(), pois a estrutura já faz este passo de forma automática.
#### Agora vamos fazer uma análise do arquivo txt colocado aqui
#### O arquivo provém do curso de Python da Hashtag treinamentos

#### repetindo o código:
````
arquivo_alunos = open('Alunos.txt', 'r')
lista_linhas = arquivo_alunos.readlines()
````
#### removendo o que é desnecessário para a análise
````
del lista_linhas[:4]
````
#### vamos definir os nossos indicadores dividindo entre contatos que foram feitos através de anuncios e de forma orgânica
````
qtde_anuncio= 0
qtde_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_site_org = 0
````
#### percorrendo a lista de linhas de forma em que possamos separar os emails da origem do dado
#### aproveitando a estrutura do for, vamos inserir condições para aproveitar a estrutura
````
for linha in lista_linhas:
    email, origem = linha.split(",")
    if '_org' in origem:
        qtde_org += 1
        if 'hashtag_yt_org' in origem:
            qtde_yt_org += 1
        if 'hashtag_site_org' in origem:
            qtde_site_org += 1
        if 'hashtag_ig_org' in origem or 'hashtag_igfb_org' in origem:
            qtde_igfb_org += 1
    else:
        qtde_anuncio += 1
````       
#### Fechando o arquivo
````
arquivo_alunos.close()
````
#### Exibindo resultados:
````
print('Quantidade anúncio: {}'.format(qtde_anuncio))
print('Quantidade orgânico: {}'.format(qtde_org))
print('Quantidade Youtube: {}'.format(qtde_yt_org))
print('Quantidade Instagram ou Facebook: {}'.format(qtde_igfb_org))
print('Quantidade Site: {}'.format(qtde_site_org))
````


#### Agora vamos exportar o resultado para um novo arquivo:
````
with open('Indicadores.txt', 'w') as arquivo_indicadores:
    arquivo_indicadores.write('Quantidade anúncio: {}\n'.format(qtde_anuncio))
    arquivo_indicadores.write('Quantidade orgânico: {}\n'.format(qtde_org))
    arquivo_indicadores.write('Quantidade Youtube: {}\n'.format(qtde_yt_org))
    arquivo_indicadores.write('Quantidade Instagram ou Facebook: {}\n'.format(qtde_igfb_org))
    arquivo_indicadores.write('Quantidade Site: {}\n'.format(qtde_site_org))
````
 
### Arquivos XML
#### Trabalharemos com XML utilizando a biblioteca xmltodict para ler notas fiscais eletrônicas (NF-e)
#### Link com os arquivos trabalhados: https://drive.google.com/drive/folders/1zhfuC67YAbAp4IUHLH8eLla-8DSOcaHQ?usp=share_link
#### Utilizando o Pycharm é possível ter uma formatação do arquivo XML diferenciada, com melhor organização
#### Para instalar iremos ao prompt e faremos:

pip install xmltodict

#### Após a biblioteca estar devidamente instalada, iremos importar a biblioteca e começar a escrever o código
#### Vamos definir uma função que seja capaz de abrir o arquivo e ler de forma binária com o método open(,'rb')
````
def ler_xml_danfe(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    # utilizando o método "print(documento)" poderemos visualizar todo o documento ordenado em dicionários ordenados baseados na árvore do XML (Xpath)
    # assim é permitido estabelecer o caminho (PATH) dentro do código para acessar certas informações
    # Para otimizar o nosso código, vamos identificar o lugar comum onde todas as informações estão:
    
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']
    
    # vamos coletar algumas informações importantes com essa função

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']
    
    # por ultimo vamos coletar os produtos da nota fiscal. Porém, diferente dos outros valores, estes são vários. 
    # Sendo assim iremos coletar o nome do produto e o valor do produto da seguinte forma:
    
    # Primeiro vamos encurtar o nosso Path    
    produtos = dic_notafiscal['det']
    
    # Criar uma lista para alocar os produtos
    lista_produtos = []
    
    # Utilizar um FOR para coletar os valores e alocar em nossa lista
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))
        
    # Por último vamos exibir os resultados coletados pra obter o resultado da função:
    resposta = {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [lista_produtos],
    }
    
    # O motivo pelo qual iremos retornar um dicionário como resposta é para que seja possível utilizar um método do Python para transformar um dicionário em uma tabela
    # O mesmo motivo pelo qual cada item do dicionário é transformado em uma lista, já que ao final da conversão a intenção é de que 1 nota fiscal seja equivalente a 1 linha do banco de dados
    return resposta
````    
#### Para termos uma ideia do resultado vamos printar o resultado enquanto chamamos a nossa função:
````
print(ler_xml_nota('NFs Finais/DANFEBrota.xml'))
````
    
#### Uma vez que estas notas fiscais eletrônicas possuem um padrão a ser seguido, é possível fazer a coleta das mesmas informações independente da nota fiscal utilizada apenas mudando o nome do arquivo.xml. 
#### Sendo assim, iremos criar um loop FOR capaz de ler todas as notas que sigam o padrão da função dentro de uma pasta de arquivos com a biblioteca OS

#### Também vamos transpor essas informações obtidas para um banco de dados, para isso iremos utilizar as bibliotecas pandas
#### Caso não esteja utilizando o Jupyter, será necessário fazer o pip install
````
import os
import pandas as pd

lista_arquivos = os.listdir('NFs Finais')
# Esta linha de código transforma em uma lista todos os arquivos dentro da pasta


df_final = pd.DataFrame()
for arquivo in lista_arquivos:
  if 'xml' in arquivo:
    if 'DANFE' in arquivo:
      df = pd.DataFrame.from_dict(ler_xml_DANFE(f'NFs Finais/{arquivo}'))
    df_final = df_final.append(df)
    
print(df_final)
df_final.to_excel('NFs.xlsx', index=False)
````



