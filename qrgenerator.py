import pyqrcode

url = input("Enter url to generate QR code: ")
print("QR code is generating...")

qr_code = pyqrcode.create(url)
qr_code.svg("qrcode.svg",background= '#ffff', scale=10)

print("QR code was generated.")