import flet as ft


def main(page: ft.Page):
    page.title = "Background Remover Pro"
    page.bgcolor = "#6868c9"
    page.window.height = 900
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.Text("Hola adentro", color="white")
    )
    page.update()


ft.app(target=main)
