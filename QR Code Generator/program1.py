# Advance Feature to create QR Code

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=15,border=5, )

qr.add_data("https://github.com/Simransonii")
qr.make(fit=True)
img=qr.make_image(fill_color="white" , back_color="orange")
img.save("another_link.png")