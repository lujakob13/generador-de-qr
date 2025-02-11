import qrcode
import validators #es una biblioteca que me valida si la url esta bien escrita

def validar_url(url):
    if validators.url(url): #si la url es valida que retorne un true
        return True
    else:
        return False # si no es valida que me retorne un false

def generar_qr(url):
    crear_qr= qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja en píxeles
    border=4,  # Borde del QR
    )
    crear_qr.add_data(url) #agrega la url al qr
    crear_qr.make(fit= True) #hace que el qr se ajuste al tamaño de la url
    img = crear_qr.make_image(fill='black', back_color='white') #crear la imagen del qr
    img.save("qr_code.png") #guardar imagen del qr
    img.show() #mostrar imagen del qr

def main():
    while True:
        url = input("ingrese la url (escriba 'salir' para terminar): ")
        if url.lower() == "salir":
            break
        if validar_url(url):
            generar_qr(url)
        else:
            print("la url no es valida")

if __name__ == "__main__":
    main()
    

