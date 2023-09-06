import pyautogui;
import time

pyautogui.alert('The automation of files to Google Drive is starting now..............')
pyautogui.PAUSE = 0.7
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(3204, 94)
pyautogui.mouseDown()
pyautogui.moveTo(2005, 1213)

pyautogui.hotkey('alt', 'tab')
time.sleep(1.5)
pyautogui.mouseUp()

time.sleep(5)

pyautogui.alert('Finished!')