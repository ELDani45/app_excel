import flet as ft

def contenido_el_club():
    return ft.Container(
        content=ft.Column([
            ft.Text("Bienvenido a la sección 'El Club'", size=30, color="green"),
            ft.Text("Aquí puedes poner información sobre el club, historia, etc.", size=20),
            ft.Text("Proximamente...")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        padding=30,
        expand=True
    )
