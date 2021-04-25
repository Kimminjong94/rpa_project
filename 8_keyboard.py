import pyautogui
w = pyautogui.getWindowsWithTitle("제목없음")[0] #메모장 1개를 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("skehzhele", interval=0.25)

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)

#특수문자
#shift 4 ->$
# pyautogui.keyDown("shift")
# pyautogui
import pyperclip
pyperclip.copy("나도코딩")
pyautogui.hotkey("ctrl","v")