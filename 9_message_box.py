import pyautogui
# print("곧 시작합니다...")
# pyautogui.countdown(3)
# print("자동화 시작")\

# # pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") #확인 버튼
# result = pyautogui.confirm("계속하실?", "확인")
# print(result)
# result = pyautogui.prompt("파일명을 뭐로 하실?", "입력")
# print(result)
result = pyautogui.password("암호를 입력하세요")
print(result)