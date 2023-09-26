import pyautogui
import time
import pandas as pd

# Passo 1: abrir o navegador.
pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('enter')                                    

time.sleep(5)
    # entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# aguardar o site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.press('tab')
pyautogui.write('fulano@gmail.com')
pyautogui.press('tab')# passa para o input senha.
pyautogui.write('senhaforte')
pyautogui.press('tab')# passa para o botão entrar.
pyautogui.press('enter')

time.sleep(4)
pyautogui.click(x=547, y=262) # busca a posição do primeiro input para iniciar o cadastro de produtos.
# Passo 3: importar a baser de dados de produtos
time.sleep(1)
tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']
    time.sleep(1)
    # Prencher os campos.
    pyautogui.click(x=547, y=262) # busca a posição do primeiro input para iniciar o cadastro de produtos.
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    if not pd.isna(obs) and obs:
        pyautogui.write(str(obs))
        pyautogui.press('tab')
        
    pyautogui.press('enter')# Enviar cadastro.

    # Volte ao topo
    pyautogui.scroll(200)

    # Imprimir valores para depuração
    #print(codigo, marca, tipo, categoria, preco_unitario, custo, obs)

print('Lista de Produtos cadastrado com sucesso!')



