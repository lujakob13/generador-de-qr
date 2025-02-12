import qrcode
import validators #es una biblioteca que me valida si la url esta bien escrita
import customtkinter as ctk

def validar_url():
    if validators.url(url_entry.get()): #si la url es valida que retorne un true
        return True
    else:
        return False # si no es valida que me retorne un false

def generar_qr():
    crear_qr= qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja en píxeles
    border=4,  # Borde del QR
    )
    crear_qr.add_data(url_entry.get()) #agrega la url al qr
    crear_qr.make(fit= True) #hace que el qr se ajuste al tamaño de la url
    #crear la imagen del qr
    img = crear_qr.make_image(fill='black', back_color='white')
    img = img.resize((200, 200))
    ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 380))
    imagen_label.configure(image=ctk_image)
    img.save("qr_code.png") #guardar imagen del qr
    "img.show()" #mostrar imagen del qr

def main():
    while True:
        url = input("ingrese la url (escriba 'salir' para terminar): ")
        if url.lower() == "salir":
            break
        if validar_url(url):
            generar_qr(url)
        else:
            print("la url no es valida")
            

#crear ventana
ventana = ctk.CTk()
ventana.title("generador de QR")
ventana.geometry("400x400")

#crear etiqueta
url = ctk.CTkLabel(ventana, text="ingrese la url")
url.pack(pady=10)

#campo de entrada
url_entry = ctk.CTkEntry(ventana, placeholder_text="url", justify= "left", width= 380)
url_entry.pack(pady=2)

#boton para crear
boton_crear= ctk.CTkButton(ventana, text = "generar", command=generar_qr)
boton_crear.pack(pady=10)

# Crear label para mostrar el QR

imagen_label = ctk.CTkLabel(ventana, text="", image=None)
imagen_label.pack(pady=20)

ventana.mainloop()

if __name__ == "__main__":
    main()
    

