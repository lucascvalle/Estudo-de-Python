### Vamos integrar o Python com o seu e-mail Outlook
#### Para isso utilizaremos a biblioteca win32com.client
#### Comecemos importando a biblioteca e abrindo o outlook
````
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'lucascvalle@outlook.com'
mail.Subject = 'Email com o CV'
mail.Body = 'O CV está anexo'

attachment = r'C:\Users\lcvalle\OneDrive\Ambiente de Trabalho\Docs\CV Lucas Costa.pdf'
mail.Attachments.Add(attachment)

mail.Send()
````
### Agora vamos aprender a "receber" e-mails, extrair anexos e informações de dentro do e-mail recebido.
#### Para isso iremos utilizar a biblioteca imap_tools, sendo necessário fazer o pip install imap_tools no prompt
#### No caso do Gmail é possível gerar uma senha de acesso especial para o e-mail a partir de um tipo de dispositivo específico que garante acesso total como a sua senha padrão
#### Gerar esta senha e substituir pela sua senha padrão.
#### No Gmail para fazer essa autorização vá em Perfil -> Gerenciar suas Configurações -> Segurança. Provavelmente será necessário fazer um processo similar em outros provedores
````
from imap_tools import MailBox, AND
````
#### Crie o acesso com seu e-mail e senha
````
usuario = "seuemail@gmail.com"
senha = 'digitesuassenha'
````

#### É necessário criar o acesso pelo "imap". Sendo que cada provedor possui um endereço diferente, é possível ver o endereço de cada um neste link:
#### https://www.systoolsgroup.com/imap/
````
meu_email = MailBox("imap.gmail.com").login(usuario, senha)
````

#### Caso o código escrito até aqui funcione, o acesso foi um sucesso, entretanto é possível que não funcione e neste caso será preciso rever as configurações de segurança.


### Agora vamos criar uma lista com todos os e-mails recebidos 
#### Com o método fetch() iremos passar os critérios que queremos para filtrar os e-mails que iremos receber junto com o método AND() que importamos no começo do código
#### É possível ver como se utiliza os métodos AND(), OR() e NOT() na documentação do Imap Tools.
````
lista_emails = meu_email.fetch(AND(from_='emailremetente@gmail.com'))
````
#### O fetch() vai transformar esse conjunto de informações em um objeto, então caso queira mostrar quantidade de informações obtidas na lista é necessário usar o método list() e len()
````
print(len(list(lista_emails)))
````

#### Agora que sabemos que a nossa lista de e-mails possui vários itens, podemos percorrer esta lista com o critério que desejarmos:
````
for email in lista_emails:
    print(email.subject)
    print(email.text)
    
    
````
#### Agora iremos coletar um anexo de um destes e-mails:
#### Uma vez que já aprendemos a criar o "filtro" para os e-mails que queremos coletar, vamos criar uma sequência de loops FOR que colete os anexos destes e-mails
````
lista_emails = meu_email.fetch(AND(from_="emaildoremetente@gmail.com"))
for email in lista_emails:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            # Podemos escrever o nome completo do arquivo, como também apenas uma parte do nome ou até mesmo apenas a extensão. Dentro da documentação da biblioteca é possível ver várias outras formas de filtrar por tipo, tamanho, etc
            if "RelatorioExcel.xlsx" in anexo.filename:
                # Aqui há um detalhe importante: O python não vai conseguir "baixar" diretamente o arquivo para o seu computador então usaremos o método .payload
                # Este método vai armazenar as informações do anexo em uma variável e depois vamos recriar o arquivo dentro do seu computador
                informacoes_anexo = anexo.payload
                with open("RelatorioExcel.xlsx", "wb") as arquivo_excel:
                    arquivo_excel.write(informacoes_anexo)
                    
````

#### O código a seguir é utilizado para enviar e-mail a partir do Gmail SEM utilizar o Outlook.
````
import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    
````
