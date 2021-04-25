from PIL.ImageOps import grayscale
import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# pyautogui.locateOnScreen("checkbox.png")



#속도개선
# 1.GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)'

#2범위개선

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x, y, width, height))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 
# run_btn = pyautogui.locate

import time
import sys