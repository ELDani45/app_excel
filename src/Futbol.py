import flet as ft


def contenido_el_futbol():
    subtitulo = ft.Text(value="Tabla de Posiciones")

    class MyButton(ft.ElevatedButton):
        def __init__(self, text, on_click=None):
            super().__init__(text=text, on_click=on_click)
            self.bgcolor = ft.Colors.ORANGE_300
            self.color = ft.Colors.GREEN_800

    def accion(Mybuttom):
        print("hola")

    tabla_posiciones = ft.Container(content=ft.Column(controls=[subtitulo]))
    return tabla_posiciones
