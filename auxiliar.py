
# Pega posição do mause na tela.
import pyautogui
import time

# Captura a tela e salva como 'screenshot.png'
time.sleep(10)
screenshot = pyautogui.screenshot()
screenshot.save('inicioCadastro.png')
pyautogui.screenshot()

#time.sleep(5)
#print(pyautogui.position())


