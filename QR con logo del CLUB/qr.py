import qrcode
from PIL import Image

imagenlogo = r'logoclub.jpeg'
logo = Image.open(imagenlogo)

# Ajustamos el tamaño de la imagen
hsize = int((float(logo.size[1])*float(100/float(logo.size[0]))))
logo = logo.resize((100, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# Llenamos de datos el código QR
#url = 'https://instagram.com/dt_uah?utm_medium=copy_link' #URL del Código
url = 'https://elcodigoascii.com.ar'
QRcode.add_data(url)
QRcode.make

# Le damos un color al código y un color al fondo
QRcolor = 'Blue'
QRfondo = 'White'

# Agregamos nuestra imagen al código QR
QRimg = QRcode.make_image(fill_color=QRcolor, back_color=QRfondo).convert('RGB')

#Establecemos la posicion de la imagen, en este caso será el centro.
pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# Guardamos la imagen de nuestro código QR en un directorio
QRimg.save(r'QR_bonito.png')