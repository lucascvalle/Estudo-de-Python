### Para fazer o a lingugagem "passear" pelo computador utilizaremos as bibliotecas pathlib e shutil
### Para fazer o download dos arquivos utilizados neste repositório acesse o link: https://drive.google.com/file/d/1XP7-Kf4qbSvKBRPD6AOdYbF9d2G0g6qp/view
### Após baixar o arquivo, descompacte-o para que torne-se uma pasta
````
from pathlib import Path
````

#### Esta primeira linha serve para mostrar o caminho (Path) onde o bloco de anotações está sendo escrito
````
print(Path.cwd())
````
#### Agora vamos acessar a nossa pasta:
#### Para isso podemos fazer de duas formas, a primeira é passando o endereço completo do diretório que queremos acessar
#### A outra é passar o caminho a partir da pasta onde o programa está sendo executado.
#### IMPORTANTE: Quando escrito no código é necessário substituir a barra inversa (\) pela barra (/), ou seu código não irá funcionar, mesmo que como resultado dos prints ainda apareça a barra.
````
caminho = Path('Arquivos_Lojas')
````
#### Vamos listar os arquivos que estão na pasta:
````
arquivos = caminho.iterdir()
for arquivo in arquivos:
    print(arquivo)
    
````
#### Vamos verificar se um arquivo específico existe dentro da pasta
````
if (caminho / Path('201801_Amazonas Shopping_AM.csv')).exists():
    print('Existe')
  
````
### Criando uma pasta e movimentando arquivos:
````
Path('Pasta').mkdir()

Path('Pasta/Pasta2').mkdir() # Para criar uma pasta dentro da pasta
````

### Agora copiando um arquivo para dentro da pasta que criamos
````
import shutil
arquivo_copiar = Path('Arquivos_Lojas/201801_Amazonas Shopping_AM.csv')
arquivo_colar = Path('Pasta/201801_Amazonas Shopping_AM_versao2.csv')
shutil.copy2(arquivo_copiar, arquivo_colar)
````
### Movendo arquivos:
````
shutil.move(Path('Pasta/201801_Amazonas Shopping_AM_versao2.csv'), Path('Pasta/Pasta2/201801_Amazonas Shopping_AM_versao2.csv'))
````
#### Agora que já sabemos como criar pastas e movimentar os arquivos dentro delas, vamo pegar todos os arquivos que estão na nossa pasta de arquivos e dividi-los de forma organizada.
#### O critério de divisão para isso serão os estados onde a rede de lojas atua.
#### RJ, SP, MG, GO, AM
````
estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
for estado in estados:
    Path('Arquivos_Lojas/{}'.format(estado)).mkdir()
    
caminho = Path('Arquivos_Lojas/')
arquivos = caminho.iterdir()
for arquivo in arquivos:
    nome_arquivo = arquivo.name
    # Para ignorar as pastas vamo fazer de forma que o código identifique que os 3 ultimos caracteres sejam .csv
    if nome_arquivo[-3:] == 'csv':
        # E para utilizar o estado para categorizar os arquivos e fazer a divisão corretamente
        estado = nome_arquivo[-6:-4]
        local_final = caminho / Path('{}/{}'.format(estado, nome_arquivo))
        shutil.move(arquivo, local_final)
````





