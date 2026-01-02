import flet as ft
import os


class BackgroundRemover:
    def __init__(self, page:ft.Page):
        self.page = page
        self.directory = None
        self.SUPPORTED_EXTENSIONS = ["png", "jpg", "jpeg", "webp"]
        self.filename_list = []
        self._setup_page()
        self._create_components()
        self._build_ui()
        
    def _setup_page(self):
        self.page.title = "Background Remover Pro"
        self.page.bgcolor = "#1a1a12e"
        self.page.window.height = 900
        self.page.window.width = 700
        self.page.theme_mode = ft.ThemeMode.DARK
    
    
    def _create_components(self):
        self.default_folder_check = ft.Checkbox(
            label="Usar carpeta predeterminada",
            value=False,
            on_change=self._checkbox_changed,
            check_color='#e94560',
            label_style=ft.TextStyle(color='#ffffff',size=14)
        )
        
        self.output_folder_textfield =ft.TextField(
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
        self.file_picker =ft.FilePicker(on_result=self.pick_files_result)
        
        self.bnt_pick_files = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.CLOUD_UPLOAD, color="#ffffff"),
                    ft.Text("Seleccionar Imágenes", color="#ffffff", weight=ft.FontWeight.BOLD),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=lambda _: self.file_picker.pick_files(
                allow_multiple=True,
                allowed_extensions=self.SUPPORTED_EXTENSIONS
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
        
        self.select_files_info = ft.Text(
        "Ningun archivo seleccionado",
        color="#a0a0a0",
        size=14,
        
    ) 
        
        self.button_remover = ft.ElevatedButton(
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
        self.page.overlay.append(self.file_picker)
    
    def _build_ui(self):
        config_card = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.SETTINGS, color="#e94560", size=20),
                    ft.Text("Configuracion", weight=ft.FontWeight.BOLD, color="#ffffff", size=16)
                ],alignment=ft.MainAxisAlignment.START),
                ft.Container(height=10),
                self.default_folder_check,
                ft.Container(height=10),
                self.output_folder_textfield,
            ], spacing=5),
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
                self.bnt_pick_files,    
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=10),
            self.select_files_info,
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
            self.button_remover,
            ft.Container(height=15),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor="#16213e",
        padding=ft.padding.all(15),
        border_radius=15,
        border=ft.border.all(1,"#0f3460"),
        width=600,
    )
        self.page.add(config_card)   
        self.page.add(files_card)
        self.page.add(process_card)

    def _checkbox_changed(self,e:ft.ControlEvent):
        self.output_folder_textfield.disabled = e.control.value
        self.output_folder_textfield.bgcolor = "#2a2a40" if not e.control.value else "#16213e"
        self.page.update()


    
    def pick_files_result(self,e):
        if e.files : 
            file_count=len(e.files)
            first_file_path = e.files[0].path
            directory = os.path.dirname(first_file_path)
            
            self.select_files_info.value=f"{file_count} archivos seleccionados\nCarpeta: {directory}"
            self.select_files_info.color="#4caf50"
            self.select_files_info.size=16
        else:
            self.select_files_info.value="Ningun archivo seleccionado"
            self.select_files_info.color="#a0a0a0"
            self.select_files_info.size=14
        self.page.update()

def main(page: ft.Page):
    obj = BackgroundRemover(page)

ft.app(target=main)

        