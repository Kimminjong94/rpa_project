from account import *
from imap_tools import MailBox

applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1
    for msg in mailbox.fetch('(SENTSINCE 17-Apr-2021'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.split("/")
            print("순번 : {} 닉네임: {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)