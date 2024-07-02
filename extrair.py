import mechanicalsoup



# Criar um navegador
browser = mechanicalsoup.StatefulBrowser()

url = "https://www.msn.com/pt-br/entretenimento/famosos/let%C3%ADcia-cazarr%C3%A9-atualiza-quadro-de-sa%C3%BAde-de-maria-guilhermina-esfor%C3%A7o-respirat%C3%B3rio-e-febre/ar-BB1nDcVC?ocid=msedgntp&pc=U531&cvid=31c2660ffb7f49c19d2e8c8693183413&ei=30"
# Abrir uma página da web
browser.open(url)

# Encontrar elementos HTML e extrair informações
headlines = browser.get_current_page().find_all(
    class_="flex flex-wrap whitespace-pre-wrap relative max-h-[calc(1.3em*3)] md:max-h-[calc(1.3em*5)] lg:max-h-[calc(1.3em*4)] overflow-y-hidden block w-full text-black font-source-code text-small-t-xs placeholder:text-black focus:outline-transparent md:text-small-t"
)
for headline in headlines:
    print(headline.text)
