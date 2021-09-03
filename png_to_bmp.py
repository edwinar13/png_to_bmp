
from PIL import Image
import os

cantidadImagenes = 10

#Recorremo la cantidad de imagenes que tenemos en la carpeta
for i in range(1,cantidadImagenes+1):

    #establecemos la ruta del las imagenes 
    path = os.path.dirname(os.path.abspath(__file__))

    #creamos los nombres de entrada y salida de las imagenes    
    if(i>=1 and i<10) :
        cantidadCeros ="000"
    elif(i>=9 and i<100):
        cantidadCeros ="00"
    elif(i>=99 and i<1000) :
        cantidadCeros ="0"
    else:
        cantidadCeros=""

    name_in = "\out{}{}.png".format(cantidadCeros,i)
    name_out = "\out{}{}.bmp".format(cantidadCeros,i)
    print(name_in,"---",name_out)
    
    #abrimos la imagen en png
    file_in = path + name_in
    img = Image.open(file_in)

    #guardamos la imagen en png
    file_out = path + name_out
    img.save(file_out)

    print("Imagen {} ok".format(i))