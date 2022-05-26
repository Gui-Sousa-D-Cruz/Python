import pyautogui
import pyperclip
import time
import pandas as pd

time.sleep (2)

pyautogui.press('win')

pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(3)


##pyautogui.hotkey("alt", "tab")

##pyautogui.hotkey("ctrl", "t")

pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')

pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')

time.sleep (3)

pyautogui.click(x=345, y=305, clicks=2)                    

time.sleep (2)

pyautogui.click(x=355, y=364)

time.sleep (2)

pyautogui.click(x=1071, y=186)

time.sleep (2)

pyautogui.click(x=852, y=624)

time.sleep(5)

tabela = pd.read_excel(r'C:\Users\ANETE\Downloads\Vendas - Dez.xlsx')


print(tabela)

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

print(faturamento)
print(quantidade)


#pyautogui.hotkey("ctrl", "t")

#pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')

#pyautogui.hotkey('ctrl', 'v')

#pyautogui.press('enter')

#time.sleep (5)