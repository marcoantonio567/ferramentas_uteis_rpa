import shutil

# Caminho da pasta de origem e destino
origem = 'caminho/para/origem'
destino = 'caminho/para/destino'

# Mover a pasta
shutil.move(origem, destino)


# __________________________________________________
#aqui ele vai renomear uma pasta 
import shutil

origem = '/home/marcos/documentos/projetos'
destino = '/home/marcos/documentos/projetos_antigos'

shutil.move(origem, destino)
# __________________________________________________
import shutil
import os

# Diretório onde estão as pastas que você quer mover
origem_base = '/home/marcos/documentos/projetos'

# Diretório para onde você quer mover as pastas
destino_base = '/home/marcos/backup/projetos'

# Itera sobre todos os itens no diretório de origem
for pasta in os.listdir(origem_base):
    # Cria o caminho completo para a pasta de origem
    origem = os.path.join(origem_base, pasta)
    # Cria o caminho completo para o destino da pasta
    destino = os.path.join(destino_base, pasta)
    # Verifica se o item é um diretório
    if os.path.isdir(origem):
        # Move o diretório de origem para o destino
        shutil.move(origem, destino)
