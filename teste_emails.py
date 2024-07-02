import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Porta 587 é utilizada com STARTTLS
smtp_user = 'seu_email@gmail.com'  # Seu endereço de email do Gmail
smtp_password = 'sua_senha_do_email'  # Senha do seu email do Gmail

# Criação do objeto para envio de email
msg = MIMEMultipart()
msg['From'] = smtp_user  # Define o remetente do email
msg['To'] = 'destinatario@example.com'  # Define o destinatário do email
msg['Subject'] = 'Assunto do Email'  # Define o assunto do email

# Corpo da mensagem
corpo_mensagem = 'Conteúdo do email aqui.'
msg.attach(MIMEText(corpo_mensagem, 'plain'))  # Adiciona o corpo da mensagem ao email

# Conexão com o servidor SMTP do Gmail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Inicia conexão TLS (para port 587)
    # Se quiser usar SSL/TLS na porta 465, descomente a linha abaixo e comente a linha acima:
    # server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_user, smtp_password)  # Faz login no servidor SMTP

    text = msg.as_string()  # Converte o objeto MIMEMultipart para string
    server.sendmail(smtp_user, 'destinatario@example.com', text)  # Envia o email

    print('Email enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar email: {str(e)}')  # Exibe mensagem de erro, se ocorrer algum problema
finally:
    server.quit()  # Encerra a conexão com o servidor SMTP
