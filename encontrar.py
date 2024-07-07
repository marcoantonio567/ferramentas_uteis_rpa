import pandas as pd
import re

#aqui ele vai fazer uma verificação pra ver se tem mais de um telefone 
def formatar_numero(numero):
  if len(numero) <= 11:
    return numero
  else:
    grupos = [numero[i : i + 11] for i in range(0, len(numero), 11)]
    return "\n".join(grupos)

# Carregar a planilha (certifique-se de que o arquivo está no mesmo diretório ou forneça o caminho completo)
file_path = 'ÁREA TÉCNICA - AGROPASSOS.xlsx'
sheet_name = 'CONCLUÍDOS AGOSTO'  # Substitua pelo nome da aba específica

# Carregar a planilha da aba específica
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)  # O header=None indica que a planilha não tem cabeçalho

def buscar_informacoes_por_cpf(cpf_informado):
    # Filtrar a linha onde o CPF (coluna 7) é igual ao CPF informado
    linha = df[df[7] == cpf_informado]

    if not linha.empty:
        # Extrair o nome (coluna 5) e telefone (coluna 12) da linha encontrada
        nome = linha.iloc[0, 5]
        telefone = linha.iloc[0, 12]
        # Verificar se o telefone está vazio
        if pd.isna(telefone) or telefone == '':
            telefone = 'vazio'
        else:
            # Extrair apenas os números do telefone
            telefone = re.sub(r'\D', '', str(telefone))
        return nome, telefone
    else:
        return None, None

# Exemplo de uso
cpf_informado = input("Informe o CPF: ")
nome, telefone = buscar_informacoes_por_cpf(cpf_informado)

if nome:
    print(f"Nome: {nome}, Telefone: {formatar_numero(telefone)}")
else:
    print("CPF não encontrado.")
