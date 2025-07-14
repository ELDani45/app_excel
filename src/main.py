import flet as ft
from el_club import contenido_el_club


def main(page: ft.Page):
   
        # PAGINA INICIO.
    def mostrar_inicio():
        page.controls.clear()  
        page.add(encabezado, banner) 
        page.update()

    def mostrar_el_club():
        page.controls.clear() 
        page.add(
            encabezado,
            contenido_el_club()  
        )
        page.update()

    # --- Función que maneja los clics en los botones del menú ---
    def on_nav_click(e):
        if e.control.text == "Inicio":
            mostrar_inicio()
        elif e.control.text == "El Club":
            mostrar_el_club()
        else:
            # Muestra un mensaje temporal para los otros botones
            page.snack_bar = ft.SnackBar(ft.Text(f"Has hecho clic en: {e.control.text}"))
            page.snack_bar.open = True
            page.update()

    #----- Textos e Imágenes del Encabezado ----#
    img1 = ft.Image(
        src="assets/cropped-deportivo_cali_logo-2-1.png",
        width=150, height=80
    )

    imgTwitter = ft.Image(src="assets/gorjeo.png", width=30, height=30)
    imgFacebook = ft.Image(src="assets/facebook.png", width=30, height=30)
    imgInstagram = ft.Image(src="assets/instagram.png", width=30, height=30)

    # --- Menú de navegación con botones interactivos ---
    textos = ft.Row(
        controls=[
            ft.TextButton("Inicio", on_click=on_nav_click),
            ft.TextButton("Comunicaciones", on_click=on_nav_click),
            ft.TextButton("El Club", on_click=on_nav_click),
            ft.TextButton("Fútbol", on_click=on_nav_click),
            ft.TextButton("Academia", on_click=on_nav_click),
            imgTwitter, imgInstagram, imgFacebook
        ],
        spacing=25,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # --- Contenedor del encabezado ---
    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                img1,
                textos
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#038345",
        padding=1,
        height=100
    )

    #---- Banner principal ----
    banner = ft.Container(
        height=200, 
        content=ft.Image(
            src="assets/x.png",
            fit=ft.ImageFit.COVER,expand=True,
            width=3000
        ),clip_behavior=ft.ClipBehavior
    )

    # --- Muestra la página principal al iniciar ---
    mostrar_inicio()

# Inicializa la app de Flet
ft.app(target=main, assets_dir="assets")
