import os

print(os.listdir('.'))   #listar arquivos do diretorio

os.mkdir('novo_diretorio') #criar uma pasta  

os.rmdir('novo_diretorio') #remover um diretorio

os.rename('novo_diretorio', 'diretorio_renomeado') #renomear um diretorio


resultado = os.popen('ls -la').read() #Executar um comando e capturar sua saída
print(resultado)


