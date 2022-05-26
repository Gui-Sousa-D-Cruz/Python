import pyautogui 
import pyperclip 
import time
import pandas as pd

time.sleep(5)

tabela = pyautogui.position()

print(tabela)

time.sleep (2)

pyautogui.press('win')

pyautogui.write('bloco')

time.sleep (2)
pyautogui.press('enter')

time.sleep(2)

pyautogui.write(str(tabela))