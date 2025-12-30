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
    page.add(btn_simple)


    btn_con_estilo = ft.ElevatedButton(
        "Seleccionar Imagen",
        on_click=simple_click,
        bgcolor="#0f3460",
        color="#ffffff",
        width=250,
        height=50,
        icon=ft.Icons.ADD
    )
    page.add(btn_con_estilo)
    page.update()


ft.app(target=main)
