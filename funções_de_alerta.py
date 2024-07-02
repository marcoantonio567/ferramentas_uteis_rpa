import pyautogui


#função de alert

#alert(text='', title='', button='OK')
#pyautogui.alert("Esta é uma mensagem de alerta.")
#-----------------------------------------------------------------------



#A função confirm()

#confirm(text='', title='', buttons=['OK', 'Cancel'])
#pergunta = pyautogui.confirm('tem um anuncio?','prvenção de falash',('sim','nao'))
#if pergunta == "sim":
    #print("voce apertou sim")
#else:
    #print("voce apertou nao")
#-----------------------------------------------------------------------



#A função prompt()

#prompt(text='', title='' , default='')

#nome = pyautogui.prompt("Qual é o seu nome?")
#print(f"Olá, {nome}!")
#-----------------------------------------------------------------------

#A função password()

#password(text='', title='', default='', mask='*')
#senha = pyautogui.password("Digite sua senha:")
#print(f"Sua senha é: {senha}")


resposta = pyautogui.alert("Como você está?")
if resposta == "OK":
    print("Achei bom saber que você está bem!")
else:
    print("O que está acontecendo?")