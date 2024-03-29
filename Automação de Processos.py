## Realização de processos de forma automatizada utilizando Python.
### Instalar Anaconda para a utilização do Jupyter como interface
#### Divisão de ações passo a passo
#### Resultado final: Envio de um e-mail
``
import pyautogui
import pyperclip
import time
# pyautogui.PAUSE = O tempo em segundos aguardados pra execução de cada ação
pyautogui.PAUSE = 0.5
``

#### Passo 1 - Entrar no Sistema.
#### Abrir o Chrome
``
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Com o chrome em foco, abrir uma nova aba
pyautogui.hotkey("ctrl", "t")

# Com a nova aba aberta, este código insere um link na barra de endereços e vai direto para ele
pyperclip.copy("link")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
``


#### Passo 2 - Navegar no Sistema
#### "import time" é utilizado para que o sistema consiga administrar o tempo de forma eficiente

``
time.sleep(5)
pyautogui.position()
# Descobrir a posição exata do mouse depois de 5 segundos

time.sleep(3)
pyautogui.click(x=,y=, clicks=2)
# Utilizado para clicar em um local específico da tela. x= posição horizontal, y= posição horizontal, clicks=numero de cliques
`` 

#### Passo 3 - Importar e Exportar bases de dados e arquivos
#### É possível utilizando os comandos .click, .press, .hotkey de acordo com a localização do arquivo no pc/web

#### Passo 4 - Calculando Indicadores
#### Sem o Jupyter, instalar o pandas, numpy e openpyxl
``

import pandas as pd
# "as pd" é apelidar o comando
arquivo = pd.read_excel(r"localdoarquivo/arquivo.xlsx, sheet=Pagina1")
# "arquivo" é o nome dado dentro do código ao arquivo que será lido pelo pandas, 
# o panda lê vários arquivos de extensões diferentes sendo "localdoarquivo/arquivo.xlsx" o local dentro do sistema onde o arquivo está, sheet= nome da página dentro do arquivo excel onde as informações estão
# o "r" é usado para caminhos de arquivo DENTRO do computador para força-lo a ler como o sistema lê
display(arquivo)

# A soma dos valores de uma coluna é feita atribuindo um nome ao resultado final e igualando esse valor baseando-se pelo nome da coluna
# no pandas ao selecionar uma coluna se utiliza colchete
# NomedoValor = arquivo=["NomedaColuna"].sum(), sendo possível também utilizar outras fórmulas como por exemplo .count()(contar), .mean()(média)
quantidade = arquivo["Quantidade"].sum()
faturamento = arquivo["Faturamento"].sum()
# display(NomedoValor) pode ser usado para conferir se a atribuição do valor está correta
`` 

#### Passo 5 - Enviar E-mail com os resultados obtidos
#### Com o Chrome em foco, repetir o processo de abertura de aba
``
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("link")
pyautogui.hotkey("ctrl", "v")
# O link em questão é o provedor de e-mail, sendo possível também adicionar mais linhas de comando para a inserção de usuário e senha utilizando o .click, .press e .write
pyautogui.press("enter")

time.sleep(5)
# Tempo definido para aguardar a página carregar corretamente
# clicar no botão de escrever
pyautogui.click(x=,y=)
# (x=,y=) é a posição do botão 
time.sleep(3)
# escrever destinatario (quem vai receber)
pyautogui.write("email")
pyautogui.press("tab")

# escrever o assunto
pyautogui.press("tab")
pyperclip.copy("Assunto do Email")
# Utilizado pyperclip.copy ao invés de pyautogui.write pois pode haver necessidade de utilizar caracteres especiais
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# escrever o corpo do email
# o f antes das 3 aspas permite que você formate o texto de forma dinâmica
texto = f"""
Prezados, bom dia.

Este é um teste em relação ao arquivo e o resultado é: R${faturamento:,.2f}
"""
# ":,.2f" é um código de formatação utilizado. Neste caso é para adicionar o separador de milhar (,), adicionar mais duas casas decimais (.2) e torna-lo um float (f)
# Agora vamos copiar o texto escrito acima e colar dentro do corpo do e-mail
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")


# enviar o email
pyautogui.hotkey("ctrl", "enter")

``
#### conferir o código sendo executado por completo


