import flet as ft
import os
from eliminador_fondos import BackgroundRemover

def main(page: ft.Page):
    page.title = "Background Remover Pro"
    page.bgcolor = "#1a1a12e"
    page.window.height = 900
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.DARK
    
    
    
    output_folder_textfield =ft.TextField(
        label="Carpeta de salida",
        width=350,
        height=60,
        autofocus=False,
        border_radius=10,
        content_padding=ft.padding.all(15),
        bgcolor="#16213e",
        color="#ffffff",
        border_color="#0f3460",
        focused_border_color="#e94560",
        #text_style=ft.TextStyle(color="#ffffff", size=14),
        #label_style=ft.TextStyle(color="#a0a0a0", size=14),
    )
    
    def _checkbox_changed(e:ft.ControlEvent):
        output_folder_textfield.disabled = e.control.value
        output_folder_textfield.bgcolor = "#2a2a40" if not e.control.value else "#16213e"
        page.update()
            
        

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
        on_change=_checkbox_changed,
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
    
    button_remover = ft.ElevatedButton(
        content=ft.Row([
            ft.Icon(ft.icons.AUTO_FIX_HIGH, color="#ffffff"),
            ft.Text("Remover Fondos", color="#ffffff", weight=ft.FontWeight.BOLD, size=10),
        ], alignment=ft.MainAxisAlignment.CENTER),
        on_click=lambda e: print("Removiendo fondos..."),
        bgcolor="#e94560",
        color="#ffffff",
        width=300,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            elevation=5
        ),
        
    )
    
    config_card =ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.icons.SETTINGS, color="#e94560", size=20),
                ft.Text("Configuracion", weight=ft.FontWeight.BOLD, color="#ffffff", size=16)
            ],alignment=ft.MainAxisAlignment.START),
            ft.Container(height=10),
            default_folder_check,
            ft.Container(height=10),
            output_folder_textfield,
        ], spacing=5
            
        ),
        bgcolor="#16213e",
        padding=ft.padding.all(15),
        border_radius=15,
        border=ft.border.all(1,"#0f3460"),
        width=600,
    )
    
    files_card =ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.icons.IMAGE, color="#e94560", size=20),
                ft.Text("Configuracion", weight=ft.FontWeight.BOLD, color="#ffffff", size=16)
            ],alignment=ft.MainAxisAlignment.START),
            ft.Container(height=15),
            ft.Row([
                bnt_pick_files,    
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=10),
            select_files_info,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor="#16213e",
        padding=ft.padding.all(15),
        border_radius=15,
        border=ft.border.all(1,"#0f3460"),
        width=600,
    )
    
    process_card =ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.icons.PSYCHOLOGY, color="#e94560", size=20),
                ft.Text("Configuracion", weight=ft.FontWeight.BOLD, color="#ffffff", size=16)
            ],alignment=ft.MainAxisAlignment.START),
            ft.Container(height=20),
            button_remover,
            ft.Container(height=15),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor="#16213e",
        padding=ft.padding.all(15),
        border_radius=15,
        border=ft.border.all(1,"#0f3460"),
        width=600,
    )
    
    page.add(config_card)     
    page.add(files_card)
    page.add(process_card)
    
    page.update()

ft.app(target=main)
