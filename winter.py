if "/".join(__import__('sys').argv[0].split("\\")).split("/")[-1] != "winter.py":
    __import__('sys')
    print("\033[1;34m[ Winter ] CÁI ĐỊT MẸ MÀY !!!!")
    print("\033[1;34m[ Winter ] Đổi tên tool thành winter.py để sử dụng !!")
    exit(1)
try:
    if "/".join(__file__.split("\\")).split("/")[-1] != "winter.py":
        __import__('sys')
        print("")
        exit(1)

except:
    pass
 
 
 
import requests, os, time
os.system("clear")
th='- - - - - - - - - - - - - - - - - - - - - - - - -'
def ban():
 print(f'''\033[1;35m
           _       __           
 _      __(_)___  / /____  _____
| | /| / / / __ \/ __/ _ \/ ___/
| |/ |/ / / / / / /_/  __/ /    
|__/|__/_/_/ /_/\__/\___/_/     
                                
\n''')
ban()
print("\033[;35mLoading.")
time.sleep(0.2)
print("\033[1;35mLoading..")
time.sleep(0.2)
print("\033[1;35mLoading...")
time.sleep(0.2)
print("\033[1;35mLoading....")
time.sleep(0.2)
print("\033[1;35mLoading.....")
time.sleep(0.2)
print("\033[1;35mLoading......")
time.sleep(0.2)
print("\033[1;35mLoading.......")
time.sleep(0.2)


os.system("clear")
print('''\033[1;35m
           _       __           
 _      __(_)___  / /____  _____
| | /| / / / __ \/ __/ _ \/ ___/
| |/ |/ / / / / / /_/  __/ /    
|__/|__/_/_/ /_/\__/\___/_/     
                                
\n''')
time.sleep(0.5)
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[1] Tool Spam Mess Ng Cao Kien")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[2] Tool Gõ Nhây")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[3] Tool Spam Discord")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[4] Exit")
chon=input('\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mNhập số: ')
so1="1"
so2="2"
so3="3"
so4="4"
if(chon==so1):
    exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/tool.py").text)
if(chon==so2):
    exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/gonhay.py").text)  
if(chon==so3):
	os.system("clear")
	exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/winter2.py").text)
if(chon==so4):
	exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/exit.py").text)
