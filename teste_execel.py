import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# esse aqui falta arrumar ainda 
# link dele que to aprendendo um pouco mais : https://www.youtube.com/watch?v=4ZSWZg2daqQ

planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']
driver = webdriver.Chrome()
driver.get('https://consultcpf-devaprender.netlify.app')
sleep(3.5)

for linha in pagina_clientes.iter_rows(min_row=2, max_row=5, values_only=True):
    nome, valor, cpf, vencimento = linha  
    
    campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="cpfInput"]')
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(cpf)
    sleep(1)
    
    botao = driver.find_element(By.XPATH, '//*[@id="consultaForm"]/button')
    botao.click()
    sleep(4)
    
    status = driver.find_element(By.XPATH, '//*[@id="statusLabel"]').text
    
    if status == "em dia":
        try:
            data_pagamento = driver.find_element(By.XPATH, '//*[@id="paymentDate"]').text.split()[3]
            metodo_pagamento = driver.find_element(By.XPATH, '//*[@id="paymentMethod"]').text.split()[4]
        except IndexError as e:
            print(f"Erro ao obter dados de pagamento para {cpf}: {e}")
            continue
        
        planilha_fechamento = openpyxl.load_workbook('planilha fechamento.xlsx')
        pagina_fechamento = planilha_fechamento['Sheet1']
        
        pagina_fechamento.append([nome, valor, cpf, vencimento, 'em dia', data_pagamento, metodo_pagamento])
        planilha_fechamento.save('planilha fechamento.xlsx')
        planilha_fechamento.close()  # Fechar a planilha após salvar
        
    else:
        planilha_fechamento = openpyxl.load_workbook('planilha fechamento.xlsx')
        pagina_fechamento = planilha_fechamento['Sheet1']
        
        pagina_fechamento.append([nome, valor, cpf, vencimento, 'pendente'])
        planilha_fechamento.save('planilha fechamento.xlsx')
        planilha_fechamento.close()  # Fechar a planilha após salvar

driver.quit()  # Fechar o navegador ao final do processo
