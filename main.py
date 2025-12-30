import flet as ft


def main(page: ft.Page):
    page.title = "Background Remover Pro"
    page.bgcolor = "#1a1a12e"
    page.window.height = 900
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.DARK
    

    # def simple_click(e):
    #     print("Hola mundo")

    #Funciones Lambda
    simple_click = lambda e: print("Hola mundo")

    btn_simple = ft.ElevatedButton(
        "Seleccionar Imagen",
        on_click=simple_click
    )
   


    btn_con_estilo = ft.ElevatedButton(
        "Seleccionar Imagen",
        on_click=simple_click,
        bgcolor="#0f3460",
        color="#ffffff",
        width=250,
        height=50,
        icon=ft.Icons.ADD
    )

    btn_profesional = ft.ElevatedButton(
        bgcolor="#0f3460",
        color="#ffffff",
        width=250,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        content=ft.Row(
            [
                ft.Text("Seleccionar Imagen", color="#ffffff", weight=ft.FontWeight.BOLD),
                ft.Icon(ft.Icons.CLOUD_UPLOAD, color="#ffffff")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(btn_simple)
    page.add(btn_con_estilo)
    page.add(btn_profesional)
   
    page.update()


ft.app(target=main)
