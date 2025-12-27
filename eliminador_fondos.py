
from pathlib import Path
from rembg import remove


class BackgroundRemover:
    
    #Variables de clase
    SUPPORTED_EXTENSIONS = ('.png','jpg','.jpeg',)
    
    def __init__(self, input_folder, output_folder):
        #Variables de instancia
        self.input_folder = input_folder
        self.output_folder = output_folder
        
    def remove_background(self,input_folder,output_folder):
        with open(input_folder, 'rb') as inp, open(output_folder,'wb') as outp:
            output = remove(inp.read())
            outp.write(output)
        
        
eliminar = BackgroundRemover('input1','input2')
print(f"Los valores de eliminar son {eliminar.input_folder} , {eliminar.output_folder}")

eliminador = BackgroundRemover('input1.png','output1.png')
eliminador.remove_background('images.png', 'mario_sinfondo.png')