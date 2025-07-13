import sys
print("Usando Python desde:", sys.executable)

import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.Colors.BLACK

    tareas = []
    
    def seleccionTarea(e):
        seleccion.value = f"Tarea seleccionada: {e.control.label}"
        page.update()

    def AgregarTarea(e):
        if campoLista.value.strip():
            nueva_tarea = ft.ListTile(
                title=ft.Checkbox(
                    label=campoLista.value, on_change=seleccionTarea, fill_color="black",border_side=ft.BorderSide(color="white", width=2),check_color="green"
                )
            )
            tareas.append(nueva_tarea)
            listaatareas.controls.clear()
            listaatareas.controls.extend(tareas)
            campoLista.value = ""
            page.update()
 

    listaatareas = ft.ListView(expand=1, spacing=5)
    t = ft.Text(value="FilTred", color="green", size=35, weight=ft.FontWeight.BOLD)

    img1 = ft.Image(
    src="assets/imagen.logo.png",
    width=180,
    height=80,
    fit=ft.ImageFit.CONTAIN 
)

    campoLista = ft.TextField(hint_text=" Escribe una tarea: ",border_color="white",focused_bgcolor="gray", text_style=ft.TextStyle(color="white"))

    boton1 = ft.FilledTonalButton(text="Agregar", on_click=AgregarTarea,width=78,height=48, bgcolor="white",color="green")

    seleccion = ft.Text(value="", size=25, weight=ft.FontWeight.BOLD,color="white")

    titulo = ft.Row(
        controls=[t, img1],
        alignment=ft.MainAxisAlignment.CENTER
    )
    colum1 = ft.Column(
        controls=[campoLista, listaatareas,seleccion], horizontal_alignment=ft.MainAxisAlignment.START, width=300
    )
    colum2 = ft.Column(
        controls=[boton1]
    )
    fila1columnas= ft.Row(
        controls=[colum1,colum2], spacing= 30,alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER,expand=True
    )

    page.add(titulo, fila1columnas)

ft.app(target=main,assets_dir="assets")
