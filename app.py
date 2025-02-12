import qrcode  # Biblioteca para generar códigos QR
import validators  # Biblioteca que valida si la url está bien escrita
import customtkinter as ctk  # Biblioteca para crear interfaces gráficas modernas

def validar_url():
    url = url_entry.get()  # Obtener la url del campo de entrada
    if not url:  # Verificar si la url está vacía
        mensaje_error.configure(text="ingrese una url valida")
        return False
    if not url.startswith(("http://", "https://")):
        url = "http://" + url  # Si no tiene http o https, se le agrega http://
    es_valida = validators.url(url)  # Verificar si la url es válida usando la biblioteca validators
    if not es_valida:
        mensaje_error.configure(text="la url no es valida")
        return False
    mensaje_error.configure(text="")  # Limpiar el mensaje de error
    return True

def generar_qr():
    crear_qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja en píxeles
    border=4,  # Borde del QR
    )
    if not validar_url():  # Validar la URL antes de generar el QR
        return
    url = url_entry.get()  # Obtener la URL del campo de entrada
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Agregar http:// si no tiene protocolo
    
    # Crear la imagen del QR
    img = crear_qr.make_image(fill='black', back_color='white')  # Generar imagen QR en blanco y negro
    img = img.resize((200, 200))  # Redimensionar la imagen
    ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 380))  # Crear imagen compatible con customtkinter
    imagen_label.configure(image=ctk_image)  # Mostrar la imagen en la interfaz
    img.save("qr_code.png")  # Guardar imagen del QR en un archivo
    "img.show()"  # Mostrar imagen del QR (comentado)

def main():
    while True:  # Bucle principal para la versión de consola
        url = input("ingrese la url (escriba 'salir' para terminar): ")
        if url.lower() == "salir":
            break
        if validar_url(url):
            generar_qr(url)
        else:
            print("la url no es valida")
            
# Configuración de la interfaz gráfica
ctk.set_appearance_mode("dark")  # Establecer modo oscuro
ctk.set_default_color_theme("blue")  # Establecer tema azul

# Crear y configurar la ventana principal
ventana = ctk.CTk()
ventana.title("Generador de Códigos QR")  # Título de la ventana
ventana.geometry("500x600")  # Tamaño de la ventana
ventana.configure(fg_color="#2b2b2b")  # Color de fondo oscuro

# Crear etiqueta para el título
url = ctk.CTkLabel(
    ventana, 
    text="Ingrese la URL", 
    font=("Helvetica", 16, "bold"),
    text_color="#ffffff"
)
url.pack(pady=20)  # Agregar espacio vertical

# Campo de entrada para la URL
url_entry = ctk.CTkEntry(
    ventana, 
    placeholder_text="https://ejemplo.com",  # Texto de ejemplo
    justify="left",
    width=400,
    height=40,
    font=("Helvetica", 14),
    corner_radius=10  # Bordes redondeados
)
url_entry.pack(pady=10)

# Botón para generar el código QR
boton_crear = ctk.CTkButton(
    ventana, 
    text="Generar QR",
    command=generar_qr,  # Función que se ejecuta al hacer clic
    font=("Helvetica", 14, "bold"),
    corner_radius=10,
    hover_color="#1f538d",  # Color al pasar el mouse
    height=40,
    width=200
)
boton_crear.pack(pady=20)

# Etiqueta para mostrar el código QR generado
imagen_label = ctk.CTkLabel(
    ventana, 
    text="", 
    image=None,
    corner_radius=15
)
imagen_label.pack(pady=30)

# Etiqueta para mostrar mensajes de error
mensaje_error = ctk.CTkLabel(
    ventana, 
    text="",
    text_color="#ff4444",  # Color rojo para errores
    font=("Helvetica", 12)
)
mensaje_error.pack(pady=10)

ventana.mainloop()  # Iniciar el bucle principal de la interfaz gráfica

if __name__ == "__main__":
    main()  # Ejecutar la función principal si el script se ejecuta directamente
    

