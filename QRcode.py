import pyqrcode

url = pyqrcode.create("www.youtube.com")
url.svg('uca-url.svg',scale=8)
print(url.terminal(quiet_zone=1))