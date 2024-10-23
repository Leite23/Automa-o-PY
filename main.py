import pyautogui
import time

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey('ctrl', 'e')
pyautogui.write("Mercado Livre")
pyautogui.press("enter")
