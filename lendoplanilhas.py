import openpyxl

#carreando arquivo
book = openpyxl.load_workbook("planilha_de_compras.xlsx")
#selecionando uma pagina
frutas_page = book['frutas']
#imprimindo os dados da cada linhas
for rows in frutas_page.iter_rows(min_row=2):
    for cell in rows:
        print(cell.value)
