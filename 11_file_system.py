#파일 기본 
import os
# print(os.getcwd()) #current working directory
# os.chdir("rpa_basic") 
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# # os.chdir("")
# # print(os.getcwd())

# 파일 경로
# open("파일경로")as
# print(os.path.join(os.getcwd(), "my_file.txt"))


#파일 경로에서 폴더정보 가져오기
# os.path.dirname(r"/Applications/Python 3.8/work spaceses/rpa_basic/2_desktop/11_file_system.py")

#파일 정보가져오기
import time
import datetime
#파일의 생성날짜
# ctime = os.path.getctime("scores.xlsx")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# mtime = os.path.getmtime("scores.xlsx")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# #파일의 마지막 접근날자
# atime = os.path.getatime("scores.xlsx")
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

#파ㅓ일 크기
# size = os.path.getsize(file_path)
# print(size)

# print(os.listdir())
# print(os.listdir("rpa_basic"))

#파일목록 가져오기(하위폴더 포함)
# result = os.walk("rpa_basic")
# # print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

#만약 폴더내에서 특정 파일들을 찾으려면 ?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     #[a.txt, b.txt, c.txrt]
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 특정 패턴을 가진 파일들을 찾으려면?
# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))
# print(result)

# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# print(os.path.isdir("run_btn.png"))
#어떤 파일을 폴더 안으로 복사하기
import shutil
# shutil.copy("trash_icon.png", "test_folder")
