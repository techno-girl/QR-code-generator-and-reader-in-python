import pyqrcode
# generate QRcode
qr=pyqrcode.create('hello')
qr.png('qrcodeimg.png',scale=8)


# read QRcode
from pyzbar.pyzbar import decode
from PIL import Image

d=decode(Image.open('qrcodeimg.png'))
print(d)
print(d[0].data.decode('ascii'))