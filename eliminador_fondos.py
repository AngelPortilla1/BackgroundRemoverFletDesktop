
from pathlib import Path
from rembg import remove


class BackgroundRemover:
    
    #Variables de clase
    SUPPORTED_EXTENSIONS = ('.png','jpg','.jpeg',)
    
    def __init__(self, input_folder, output_folder):
        #Variables de instancia
        self.input_folder = input_folder
        self.output_folder = output_folder
        
    def process_images(self, filename_list,process_callback=None):
        pass
    
    
    def _is_supported_image(self, filename:str):
        
        return filename.lower().endswith.(self.SUPPORTED_EXTENSIONS)
        
    
    def _remove_background(self, input_path, output_path):
        with open(input_path, 'rb') as inp, open(out_path, 'wb') as outb:
            output = remove(inp.read())
            outb.write(ouput)
        
    
    
    def _move_original(self, input_path):
        original_folder = self._processed_folder / "originals"
        original_folder.mkdir()(exist_ok=True)
        new_path = original_folder / input_path.name
        input_path.rename(new_path)
                
        
        