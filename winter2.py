import requests
import random
import time
import os
from colorama import Fore

print("\033[1;35m===========================================")
print('\033[1;34m[ WINTER ] Tool Spam Discord > WINTER ON TOP')
print("\033[1;35m===========================================\n")

time.sleep(1)

channel_id = input("\033[1;34m[ WINTER ] Nhập ID kênh: ")
waktu1 = int(input("\033[1;34m[ WINTER ] Đặt thời gian gui tin nhắn: "))

time.sleep(0.5)
print("\033[1;34m[ WINTER ] loading.")
time.sleep(0.5)
print("\033[1;34m[ WINTER ] loading..")
time.sleep(0.5)
print("\033[1;34m[ WINTER ] loading...")
time.sleep(0.5)
print("\033[1;34m[ WINTER ] loading....")
time.sleep(0.5)
print("\033[1;34m[ WINTER ] loading.....")
time.sleep(0.5)

os.system('cls' if os.name == 'nt' else 'clear')

with open("noidung.txt" , "r") as f:
    words = f.readlines()

with open("token.txt" , "r") as f:

    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.YELLOW + "\033[1;34m[ WINTER ] Spam Thành Công !!")
        #print(Fore.YELLOW + payload['[ WINTER ] Spam.... Thanh Cong'])
        time.sleep(waktu1)

       # response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

