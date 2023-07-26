import qrcode
import webbrowser

# Creamos el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Añadimos el contenido al QR
qr.add_data("https://github.com/puchiflito/Pruebas")

# Hacemos el proceso de dibujo
qr.make(fit=True)

# Obtenemos la imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Mostramos la imagen del QR
img.show()

# Abrimos el archivo HTML al escanear el QR
webbrowser.open("https://github.com/puchiflito/Pruebas")
