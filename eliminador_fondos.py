
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
    
    
    def _is_supported_image(self, filename):
        pass
    
    def _remove_background(self, input_path, output_path):
        pass
    
    
    def _move_original(self, input_path):
        pass
        
        
        