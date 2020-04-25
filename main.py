from gi.repository import Gtk
import numpy as np
import os
from keras.preprocessing.image import load_img, img_to_array
import keras 
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform


def seleccionar_foto(button):
    selector.show_all()


def predict(file):
    x = load_img(file, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arreglo = cnn.predict(x) #[[1, 0 , 0]]
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)
    if respuesta == 0:
        print("fresa")
    elif respuesta ==1:
        print("otro")
    return respuesta


    
def seleccionar(button):
    archivo = selector.get_filename()
    etiqueta_nombre_archivo = builder.get_object("etiqueta_nombre_archivo")
    etiqueta_nombre_archivo.set_text(archivo)
    selector.hide()
    x = load_img(archivo, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = cnn.predict(x)
    result = array[0]
    answer = np.argmax(result)
    es_fresa = builder.get_object("etiqueta_es_fresa")
    etapa = builder.get_objcet("etiqueta_etapa")
    edad = builder.get_object("etiqueta_edad")
    if answer < 5:
        etapa.set_text("SI")
        if answer == 0:
            etapa.set_text("Estolon")
            edad.set_text("120-146 dias")
        if answer == 1:
            etapa.set_text("Flor")
            edad.set_text("146-192 dias")
        if answer == 2:
            etapa.set_text("Fruto")
            edad.set_text("192-220 dias")
        if answer == 3:
            etapa.set_text("Hija")
            edad.set_text("0-63 dias")
        if answer == 4:
            etapa.set_text("Hojas/Recuperacion")
            edad.set_text("63-120 dias")
    else:
        etapa.set_text("NO")
        etapa.set_text("N/A")
        edad.set_text("N/A")
            
            
        
def cancelar(button):
    selector.hide()
    
def cambiar_blanco(button):
    encabezado = builder.get_object("img_head")
    img_boton = builder.get_object("img_boton")
    img_fresa = builder.get_object("img_es_fresa")
    img_estado = builder.get_object("img_estad")
    img_edad= builder.get_object("img_edad")
    separador1 = builder.get_object("separacion1")
    separador2 = builder.get_object("separador2")
    footer = builder.get_object("img_footer")
    encabezado.set_from_file('./imagenes/head_b.png')
    footer.set_from_file('./imagenes/footer_b.png')
    img_boton.set_from_file('./imagenes/seleccionar_b.png')
    img_edad.set_from_file('./imagenes/edad_b.png')
    img_estado.set_from_file('./imagenes/etapa_b.png')
    img_fresa.set_from_file('./imagenes/es_fresa_b.png')
    separador1.set_from_file('./imagenes/separador_b.png')
    separador2.set_from_file('./imagenes/separador_b.png')
    
def cambiar_negro(button):
    encabezado = builder.get_object("img_head")
    img_boton = builder.get_object("img_boton")
    img_fresa = builder.get_object("img_es_fresa")
    img_estado = builder.get_object("img_estad")
    img_edad= builder.get_object("img_edad")
    separador1 = builder.get_object("separacion1")
    separador2 = builder.get_object("separador2")
    footer = builder.get_object("img_footer")
    encabezado.set_from_file('./imagenes/head_n.png')
    footer.set_from_file('./imagenes/footer_n.png')
    img_boton.set_from_file('./imagenes/seleccionar_n.png')
    img_edad.set_from_file('./imagenes/edad_n.png')
    img_estado.set_from_file('./imagenes/etapa_n.png')
    img_fresa.set_from_file('./imagenes/es_fresa_n.png')
    separador1.set_from_file('./imagenes/separador_n.png')
    separador2.set_from_file('./imagenes/separador_n.png')

builder = Gtk.Builder()
builder.add_from_file("./interfaz.glade")
handlers = {
    "terminar_aplicacion": Gtk.main_quit,
    "seleccionar_archivo": seleccionar_foto,
    "seleccionar": seleccionar,
    "cancelar": cancelar,
    "cambiar_blanco": cambiar_blanco,
    "cambiar_negro": cambiar_negro
}
builder.connect_signals(handlers)
window = builder.get_object("ventana_principal")
selector = builder.get_object("selector_archivos")
filtro = Gtk.FileFilter.new()
filtro.set_name("imagenes(.jpg, .png, .jpeg)")
filtro.add_pattern("*.[jpg][png][jpeg]")
selector.set_filter(filtro)
longitud = 150
altura = 150
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'
# para usuarios de pyhon 3.8 descomentar el siguiente coigo
# with CustomObjectScope({'GlorotUniform': glorot_uniform}):
    # cnn = keras.models.load_model('./modelo/modelo.h5', compile= False)
# y comentar unicamente la siguiente linea
cnn = keras.models.load_model(modelo)
cnn.load_weights (pesos)
window.show_all()
Gtk.main()