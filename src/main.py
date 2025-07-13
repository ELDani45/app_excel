import flet as ft


def Main(page: ft.Page):
    
    #----- Textos y Imagenes Del Encabezado ----#
    img1= ft.Image(
        src="/assets/imgagen.logo.png",
        width= 300, height= 200
    )
    # ENCABEZADO
    Encabezado = ft.Container(
        content= ft.Row(
            controls=[img1]
        )
        
    )

    page.add(Encabezado)
    ft.app(target=Main, assets_dir="assets")