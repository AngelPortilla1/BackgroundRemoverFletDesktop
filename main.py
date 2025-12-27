import flet as ft


def main(page: ft.Page):
    page.title = "Hola mundo"
    page.add(
        ft.Text("Hola adentro", color="white")
    )
    page.update()


ft.app(target=main)
