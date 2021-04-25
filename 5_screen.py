import pyautogui

# img = pyautogui.screenshot()
# img.save("screen shot.png")

# pyautogui.mouseInfo()
# 143,9 NA_on_macOS NA_on_macOS

pixel = pyautogui.pixel(143,9)
print(pixel)

# print(pyautogui.pixelMatchesColor(143, 9, (149, 190, 213)))
print(pyautogui.pixelMatchesColor(143, 9, (149, 190, 214)))