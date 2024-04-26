import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
banner = f"""\033[1;35m
           _       __           
 _      __(_)___  / /____  _____
| | /| / / / __ \/ __/ _ \/ ___/
| |/ |/ / / / / / /_/  __/ /    
|__/|__/_/_/ /_/\__/\___/_/     
                                
\n"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0003)
menu=f"""
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY      \033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
for h in menu:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0005)
ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'SPV/'+key1
keyv1 = 'vip789'
url = 'https://webkey38737.000webhostapp.com/key.html?'+key
token_link1s = '65bb5c09fdd913299e7c862f'
link1s = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link1s}&url={url}').json()
if link1s['status']=="error": 
    print(link1s['message'])
    quit()
else:
    link_key=link1s['shortenedUrl']
h=open('keySPV.txt',mode='a+')
h=open('keySPV.txt',mode='r')
thien=h.read()
h.close()
print()
if thien== keyv1 or thien== key:
    print(dau,'\033[1;33mWelcome🟢🟣🟡🟠🔵🟢🟡🟠🔵🟢 ')
    sleep(1)
    exec(requests.get('https://raw.githubusercontent.com/LyHoangKhangDVL/Tool/main/main').text)
else:
     print(dau,'\033[1;32mTool Spam Messenger !')
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
     print(dau,'\033[1;32mMua Key Liên Hệ Admin : https://www.facebook.com/profile.php?id=61553155932204&mibextid=ZbWKwL')
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau,'\033[1;33mLink Lấy Key Tool:\033[1;31m '+link_key)
keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mINPUT KEY TOOL\033[1;33m ~>\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
if keynhap == key or keynhap== keyv1:
    print(dau,'\033[1;32mKey Đúng !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(2)
    h=open('keySPV.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://raw.githubusercontent.com/LyHoangKhangDVL/Tool/main/main').text)
else:
    print(dau,'\033[1;33mKey Sai !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    
