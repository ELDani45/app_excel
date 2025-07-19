# import asyncio
# import flet as ft

# async def main(page: ft.Page):
#     page.bgcolor = ft.Colors.BLACK

#     progreso = ft.ProgressBar(width=400, color=ft.Colors.GREEN_ACCENT_400)
#     cargando_texto = ft.Text("Cargando tareas...", color="white", size=20)

#     page.add(
#     ft.Container(
#         content=ft.Column(
#             controls=[progreso, cargando_texto],
#             alignment=ft.MainAxisAlignment.CENTER
#         ),
#         alignment=ft.alignment.top_center,
#         expand=True
#     )
# )
#     for i in range(21):
#         progreso.value = i / 20
#         cargando_texto.value = f"Cargando... {i*5}%"
#         page.update()
#         await asyncio.sleep(0.1)

#     page.controls.clear()

#     # ---------- UI PRINCIPAL ----------
#     tareas = []

#     def seleccionTarea(e):
#         seleccion.value = f"Tarea seleccionada: {e.control.label}"
#         page.update()

#     def AgregarTarea(e):
#         if campoLista.value.strip():
#             nueva_tarea = ft.ListTile(
#                 title=ft.Checkbox(
#                     label=campoLista.value,
#                     on_change=seleccionTarea,
#                     fill_color="black",
#                     border_side=ft.BorderSide(color="white", width=2),
#                     check_color="green"
#                 )
#             )
#             tareas.append(nueva_tarea)
#             listaatareas.controls.clear()
#             listaatareas.controls.extend(tareas)
#             campoLista.value = ""
#             page.update()

#     listaatareas = ft.ListView(expand=0, spacing=5)

#     t = ft.Text(
#         value="FilTred",
#         color="green",
#         size=30,
#         weight=ft.FontWeight.BOLD
#     )
#     img1 = ft.Image(
#         src="assets/imagen.logo.png",
#         width=180,
#         height=80,
#         fit=ft.ImageFit.CONTAIN
#     )
#     titulo = ft.Container(
#         content=ft.Row(
#             controls=[t, img1],
#             alignment=ft.MainAxisAlignment.CENTER,
#         ),
#         padding=ft.Padding(top=49,bottom=9, left=20, right=20),
#     )

#     campoLista = ft.TextField(
#         hint_text=" Escribe una tarea: ",
#         border_color="white",
#         focused_bgcolor="gray",
#         text_style=ft.TextStyle(color="white")
#     )

#     boton1 = ft.FilledTonalButton(
#         text="Agregar", on_click=AgregarTarea, width=78, height=48,
#         bgcolor="black", color="green",
#         style=ft.ButtonStyle(
#             shape=ft.RoundedRectangleBorder(radius=10),
#             side=ft.BorderSide(width=2, color="white")
#         )
#     )

#     seleccion = ft.Text(value="", size=25, weight=ft.FontWeight.BOLD, color="white")

#     colum1 = ft.Container(
#         content=ft.Column(
#         controls=[campoLista, listaatareas, seleccion],
#         width=300
#         ), padding=ft.Padding(10,10,10,10)
#     )

#     column2 = ft.Container(
#         content=ft.Column(
#             controls=[boton1],
#             alignment=ft.MainAxisAlignment.START
#         ),border_radius=3,padding=ft.Padding(10,10,10,10)
#     )

#     fila1columnas = ft.Row(
#         controls=[colum1, column2],
#         vertical_alignment=ft.CrossAxisAlignment.START,
#         alignment=ft.CrossAxisAlignment.CENTER,
#         spacing=10
#     )
#     subCont = ft.Container(
#         content=ft.Text(
#             value="Subtitulo", size=20, color="white", weight=ft.FontWeight.BOLD
#         ),margin=ft.Margin(100,5,0,0)
#     )

#     cuadro = ft.Container(
#         content=ft.Column(
#             controls=[subCont, fila1columnas],
#             width=500,
#             height=400,
#             spacing=2
#         ),#              izq,up,bottom,der
#         margin=ft.Margin(50,20,10,20), bgcolor="Dark",border=ft.border.all(3,ft.Colors.WHITE), border_radius=10
#     )

#     page.add(titulo, cuadro)

# ft.app(target=main, assets_dir="assets")
