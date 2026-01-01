import flet as ft
import os
from eliminador_fondos import BackgroundRemover

def main(page: ft.Page):
    page.title = "Background Remover Pro"
    page.bgcolor = "#1a1a12e"
    page.window.height = 900
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.DARK
    

    # def simple_click(e):
    #     print("Hola mundo")

    #Funciones Lambda
    # simple_click = lambda e: print("Hola mundo")

    # btn_simple = ft.ElevatedButton(
    #     "Seleccionar Imagen",
    #     on_click=simple_click
    # )
   


    # btn_con_estilo = ft.ElevatedButton(
    #     "Seleccionar Imagen",
    #     on_click=simple_click,
    #     bgcolor="#0f3460",
    #     color="#ffffff",
    #     width=250,
    #     height=50,
    #     icon=ft.Icons.ADD
    # )

    # btn_profesional = ft.ElevatedButton(
    #     bgcolor="#0f3460",
    #     color="#ffffff",
    #     width=250,
    #     height=50,
    #     style=ft.ButtonStyle(
    #         shape=ft.RoundedRectangleBorder(radius=10)
    #     ),
    #     content=ft.Row(
    #         [
    #             ft.Text("Seleccionar Imagen", color="#ffffff", weight=ft.FontWeight.BOLD),
    #             ft.Icon(ft.Icons.CLOUD_UPLOAD, color="#ffffff")
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )
    # page.add(btn_simple)
    # page.add(btn_con_estilo)
    # page.add(btn_profesional)
   
    # page.update()
    
    
    default_folder_check = ft.Checkbox(
        label="Usar carpeta predeterminada",
        value=False,
        on_change=lambda e: print(f"Checkbox value: {e.control.value}"),
        check_color='#e94560',
        label_style=ft.TextStyle(color='#ffffff',size=14)
    )
    select_files_info = ft.Text(
        "Ningun archivo seleccionado",
        color="#a0a0a0",
        size=14,
        
    ) 

    def pick_files_result(e):
        if e.files : 
            file_count=len(e.files)
            first_file_path = e.files[0].path
            directory = os.path.dirname(first_file_path)
            
            select_files_info.value=f"{file_count} archivos seleccionados\nCarpeta: {directory}"
            select_files_info.color="#4caf50"
            select_files_info.size=16
        else:
            select_files_info.value="Ningun archivo seleccionado"
            select_files_info.color="#a0a0a0"
            select_files_info.size=14
        page.update()

    file_picker = ft.FilePicker()
    file_picker.on_result = pick_files_result
    page.overlay.append(file_picker)

    bnt_pick_files = ft.ElevatedButton(
    content=ft.Row(
        [
            ft.Icon(ft.icons.CLOUD_UPLOAD, color="#ffffff"),
            ft.Text("Seleccionar Imágenes", color="#ffffff", weight=ft.FontWeight.BOLD),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ),
    on_click=lambda _: file_picker.pick_files(
        allow_multiple=True,
        allowed_extensions=BackgroundRemover.SUPPORTED_EXTENSIONS
    ),
    bgcolor="#0f3460",
    color="#ffffff",
    width=250,
    height=50,
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        elevation=5
    ),
)
    page.add(default_folder_check)
    page.add(select_files_info)
    page.add(bnt_pick_files)
    page.update()

ft.app(target=main)
