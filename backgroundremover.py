
from pathlib import Path
from rembg import remove
import datetime


class BackgroundRemover:
    
    #Variables de clase
    SUPPORTED_EXTENSIONS = ('.png','jpg','.jpeg','bmp')
    
    def __init__(self, input_folder, output_folder):
        #Variables de instancia
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        
    def process_images(self, filename_list,progress_callback=None): #Output:/2026-12-01
        today_date = datetime.datetime.now().strftime('%Y-%m-%d_H-%M-%S')
        self._processed_folder= self.output_folder / today_date
        self._processed_folder.mkdir(parents = True, exist_ok = True)
        
        total_files = len(filename_list)
        processed = 0
        
        for filename in filename_list: 
            if self._is_supported_image(filename):
                input_path = self.input_folder / filename #descargas/imagen1.png
                output_path = self._processed_folder / filename
                
                try :   
                    self._remove_background(input_path, output_path)
                    self._move_original(input_path)
                    processed += 1
                    if progress_callback:
                        progress_callback(processed,total_files,filename)
                        
                except Exception as e:
                    print(f"Hay un error: {e}")
                    processed += 1
                    if progress_callback:
                        progress_callback(processed,total_files,f"Error: {filename}")
                    
            
    
    def _is_supported_image(self, filename:str):
        
        return filename.lower().endswith(self.SUPPORTED_EXTENSIONS)
        
    
    def _remove_background(self, input_path, output_path):
        with open(input_path, 'rb') as inp, open(output_path, 'wb') as outb:
            output = remove(inp.read())
            outb.write(output)
        
    
    def _move_original(self, input_path):
        original_folder = self._processed_folder / "originals"
        original_folder.mkdir(parents=True, exist_ok=True)
        new_path = original_folder / input_path.name
        input_path.rename(new_path)
                
        
# obj = BackgroundRemover(Path(r"D:\Angel Fuhrer\Programacion\Proyectos\Proyectos 2025-2\AppFletDesktop"), Path(r"D:\Angel Fuhrer\Programacion\Proyectos\Proyectos 2025-2\AppFletDesktop/output"))
# obj.process_images(['Captura.PNG'])