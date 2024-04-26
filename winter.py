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
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[1] Tool Spam Mess")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[2] Tool Gõ Nhây")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[3] Tool Spam Discord")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[4] Tool Spam Mess ngcaokien")
print ("\033[1;31m[👾\033[1;31m] \033[1;37m=> \033[1;33m[5] Exit\n")
chon=input('\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mNhập số: ')
so1="1"
so2="2"
so3="3"
so4="4"
so5="5"
if(chon==so1):
      os.system("clear")
      print('''\033[1;35m
           _       __           
 _      __(_)___  / /____  _____
| | /| / / / __ \/ __/ _ \/ ___/
| |/ |/ / / / / / /_/  __/ /    
|__/|__/_/_/ /_/\__/\___/_/     
                                
\n''')
time.sleep(1)
os.system("clear")

if(chon==so2):
    exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/gonhay.py").text)  
if(chon==so3):
	exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/winter2.py").text)
if(chon==so4):
	exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/tool.py").text)
if(chon==so5):
	exec(requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/exit.py").text)
print('''\033[1;35m
           _       __           
 _      __(_)___  / /____  _____
| | /| / / / __ \/ __/ _ \/ ___/
| |/ |/ / / / / / /_/  __/ /    
|__/|__/_/_/ /_/\__/\___/_/     
                                
\n''')
time.sleep(0.2)
print("\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mBạn Đã Chọn Tool Spam !!")
time.sleep(1)
id=input('\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mNhập ID Nhóm Cần Spam\033[1;37m: ')
while True:
    ck=input('\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mNhập Cookie Facebook\033[1;37m: ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        os.system('clear')
        break
    except:
        print('\033[1;31m[👾️️\033[1;31m] \033[1;37m=> \033[1;31mCookie sai!!')
    


print('''\033[1;35m
           _       __           
 _      __(_)___  / /____  _____
| | /| / / / __ \/ __/ _ \/ ___/
| |/ |/ / / / / / /_/  __/ /    
|__/|__/_/_/ /_/\__/\___/_/     
                                
\n''')
nd = (input("\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mNội Dung : "))
soluong = int(input("\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mSố Lượng : "))
delay = float(input("\033[1;31m[👾️\033[1;31m] \033[1;37m=> \033[1;33mDelay: "))
os.system("clear")
params = {
	"icm": '1',
}

headers = {
	"Host":"mbasic.facebook.com",
	"content-length":"247",
	"content-type":"application/x-www-form-urlencoded",
	"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
	"cookie":ck,
}
data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{id}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
for i in range(soluong):
	rq = requests.post("https://mbasic.facebook.com/messages/send/",params=params,headers=headers,data=data)
	print("\033[1;31m Spam:",i+1)
	time.sleep(delay)


