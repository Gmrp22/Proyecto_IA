from gi.repository import Gtk
import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as Back
import json


Back.clear_session()





def seleccionar_carpeta_validacion(button):
    seleccionador_datos_val.show_all()
def seleccionar_carpeta_datos(button):
    seleccionador_dato.show_all()
def seleccionar_carpeta_guardar(button):
    seleccionador_carpeta_guardar.show_all();
def entrenar_red(button):
    Datos_entrenamiento = etq_dir_datos.get_text()
    Datos_validacion = etq_dir_validacion.get_text()
    Carpeta_destino = etq_ruta_guardar.get_text()
    epocas= int(ent_numero_epocas.get_text())
    longitud = int(ent_altura.get_text())
    altura = int(ent_altura.get_text())
    batch_size = int(ent_tamano_lote.get_text())
    pasos = int(ent_no_pasos.get_text())    
    Pasos_validacion= int(ent_pasos_val.get_text())
    clases = int(ent_no_categorias.get_text())
    learningRate = float(ent_lr.get_text())
    entrenamiento_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2, #0.3
        zoom_range=0.2, #0.3
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(
        rescale=1. / 255)
    entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    Datos_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')
    
    validacion_generador = test_datagen.flow_from_directory(
    Datos_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')
    
    cnn = Sequential()
    cnn.add(Convolution2D(filtrosConv1, Size_filtro1, padding ="same", input_shape=(longitud, altura, 3), activation='relu'))


    cnn.add(MaxPooling2D(pool_size=Size_pool))

    cnn.add(Convolution2D(filtrosConv2, Size_filtro2, padding ="same"))
    #cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ="same", activation='relu'))
    cnn.add(MaxPooling2D(pool_size=Size_pool))
    #CLASIFICACION

    cnn.add(Flatten())
    cnn.add(Dense(256, activation='relu'))
    cnn.add(Dropout(0.5))
    cnn.add(Dense(clases, activation='softmax'))

    #PARAMETROS PARA OPTIMIZAR
    # Para usuarios de pythjonr 3.8 descomentar el siguiente codigo
    # cnn.compile(loss='categorical_crossentropy',
    #             optimizer=optimizers.Adam(learning_rate=learningRate),
    #             metrics=['accuracy'])
    # y comentar el siguietne codigo de cnn.compile
    cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizers.Adam(lr=learningRate),
            metrics=['accuracy'])


    #Correr pasos en epocas y va pasando

    cnn.fit_generator(
        entrenamiento_generador,
        steps_per_epoch=pasos,
        epochs=epocas,
        validation_data=validacion_generador,
        validation_steps=Pasos_validacion)

    #Guardar pesos finales en archivo
    
    if not os.path.exists(Carpeta_destino):
        os.mkdir(Carpeta_destino)
    save_modelo = Carpeta_destino + "/modelo.h5"
    cnn.save(save_modelo)
    save_pesos = Carpeta_destino + "/pesos.h5"
    cnn.save_weights(save_pesos)
    configuraciones = {}
    configuraciones['valores'] = []
    configuraciones['valores'].append({
            'altura' : altura,
            'longitud' : longitud,
            'batch_size': batch_size,
            'pasos': pasos,
            'validacion': Pasos_validacion,
            'learningRate': learningRate,
            'clases': clases,
            'epocas': epocas
            
    })
    guaradr_json = Carpeta_destino + "/configuraciones.json"
    with open(guaradr_json, 'w') as file:
        json.dump(configuraciones, file, indent=4)

def seleccionar_datos_val(button):
    Datos_validacion = seleccionador_datos_val.get_current_folder()
    etq_dir_validacion.set_text(Datos_validacion)
    seleccionador_datos_val.hide()
def cancelar_datos_val(button):
    seleccionador_datos_val.hide()
def seleccionar_datos(button):
    Datos_entrenamiento = seleccionador_dato.get_current_folder()
    etq_dir_datos.set_text(Datos_entrenamiento)
    seleccionador_dato.hide()
def cancelar_datos(button):
    seleccionador_dato.hide()
def cancelar_carpeta_guardar(button):
    seleccionador_carpeta_guardar.hide()
def guardar_carpeta_guardar(button):
    Carpeta_destino = seleccionador_carpeta_guardar.get_current_folder()
    Carpeta_destino = Carpeta_destino + "/modelo"
    etq_ruta_guardar.set_text(Carpeta_destino)
    seleccionador_carpeta_guardar.hide()
def cambiar_blanco(button):
    heading = builder.get_object("header")
    separador = builder.get_object("separador")
    separador1 = builder.get_object("separado1")
    titulo_imagen = builder.get_object("titulo_imagen")
    img_ancho =builder.get_object("img_ancho")
    img_altura=builder.get_object("img_altura")
    img_no_categorias = builder.get_object("img_no_categorias")
    img_bot_selec_val = builder.get_object("img_bot_selc_val")
    img_bot_selec_datos = builder.get_object("img_bot_selc_datos")
    titulo_entrenamiento = builder.get_object("titulo_entrenamiento")
    img_no_pasos = builder.get_object("img_no_pasos")
    img_no_pasos_validacion = builder.get_object("img_no_pasos_validacion")
    img_no_epocas = builder.get_object("img_no_epocas")
    img_tamano_lote = builder.get_object("img_tamano_lote")
    img_lr = builder.get_object("img_lr")
    titulo_almacenamiento = builder.get_object("titulo_almacenamiento")
    img_btn_grd = builder.get_object("img_btn_grd")
    img_entrenar_cnn = builder.get_object("img_entrenar_cnn")
    footer = builder.get_object("footer")
    heading.set_from_file("./imagenes_entrenar/header_b.png")
    separador.set_from_file("./imagenes_entrenar/separador_b.png")
    separador1.set_from_file("./imagenes_entrenar/separador_b.png")
    titulo_imagen.set_from_file("./imagenes_entrenar/titulo_imagenes_b.png")
    img_ancho.set_from_file("./imagenes_entrenar/ancho_b.png")
    img_altura.set_from_file("./imagenes_entrenar/altura_b.png")
    img_no_categorias.set_from_file("./imagenes_entrenar/numero_categorias_b.png")
    img_bot_selec_val.set_from_file("./imagenes_entrenar/seleccion_validacion_b.png")
    img_bot_selec_datos.set_from_file("./imagenes_entrenar/seleccion_datos_b.png")
    titulo_entrenamiento.set_from_file("./imagenes_entrenar/titulo_entrenamiento_b.png")
    img_no_pasos.set_from_file("./imagenes_entrenar/numero_pasos_b.png")
    img_no_pasos_validacion.set_from_file("./imagenes_entrenar/numero_pasos_validacion_b.png")
    img_no_epocas.set_from_file("./imagenes_entrenar/numero_epocas_b.png")
    img_tamano_lote.set_from_file("./imagenes_entrenar/tamano_lote_b.png")
    img_lr.set_from_file("./imagenes_entrenar/lr_b.png")
    titulo_almacenamiento.set_from_file("./imagenes_entrenar/titulo_almacenamiento_b.png")
    img_btn_grd.set_from_file("./imagenes_entrenar/img_carpeta_grd_arch_b.png")
    img_entrenar_cnn.set_from_file("./imagenes_entrenar/img_btn_entrenar_cnn_b.png")
    footer.set_from_file("./imagenes_entrenar/footer_b.png")

def cambiar_negro(button):

    heading = builder.get_object("header")
    heading.set_from_file("./imagenes_entrenar/header_n.png")
    footer = builder.get_object("footer")
    footer.set_from_file("./imagenes_entrenar/footer_n.png")
    separador = builder.get_object("separador")
    separador1 = builder.get_object("separado1")
    separador.set_from_file("./imagenes_entrenar/separador_n.png")
    separador1.set_from_file("./imagenes_entrenar/separador_n.png")
    titulo_imagen = builder.get_object("titulo_imagen")
    img_ancho =builder.get_object("img_ancho")
    img_altura=builder.get_object("img_altura")
    img_no_categorias = builder.get_object("img_no_categorias")
    img_bot_selec_val = builder.get_object("img_bot_selc_val")
    titulo_imagen.set_from_file("./imagenes_entrenar/titulo_imagenes_n.png")
    img_ancho.set_from_file("./imagenes_entrenar/ancho_n.png")
    img_altura.set_from_file("./imagenes_entrenar/altura_n.png")
    img_no_categorias.set_from_file("./imagenes_entrenar/numero_categorias_n.png")
    img_bot_selec_val.set_from_file("./imagenes_entrenar/seleccion_validacion_n.png")
    img_bot_selec_datos = builder.get_object("img_bot_selc_datos")
    titulo_entrenamiento = builder.get_object("titulo_entrenamiento")
    img_no_pasos = builder.get_object("img_no_pasos")
    img_no_pasos_validacion = builder.get_object("img_no_pasos_validacion")
    img_bot_selec_datos.set_from_file("./imagenes_entrenar/seleccion_datos_n.png")
    titulo_entrenamiento.set_from_file("./imagenes_entrenar/titulo_entrenamiento_n.png")
    img_no_pasos.set_from_file("./imagenes_entrenar/numero_pasos_n.png")
    img_no_pasos_validacion.set_from_file("./imagenes_entrenar/numero_pasos_validacion_n.png")
    img_no_epocas = builder.get_object("img_no_epocas")
    img_tamano_lote = builder.get_object("img_tamano_lote")
    img_lr = builder.get_object("img_lr")
    titulo_almacenamiento = builder.get_object("titulo_almacenamiento")
    img_btn_grd = builder.get_object("img_btn_grd")
    img_entrenar_cnn = builder.get_object("img_entrenar_cnn")
    img_no_epocas.set_from_file("./imagenes_entrenar/numero_epocas_n.png")
    img_tamano_lote.set_from_file("./imagenes_entrenar/tamano_lote_n.png")
    img_lr.set_from_file("./imagenes_entrenar/lr_n.png")
    titulo_almacenamiento.set_from_file("./imagenes_entrenar/titulo_almacenamiento_n.png")
    img_btn_grd.set_from_file("./imagenes_entrenar/img_carpeta_grd_arch_n.png")
    img_entrenar_cnn.set_from_file("./imagenes_entrenar/img_btn_entrenar_cnn_n.png")
    
    
builder = Gtk.Builder()
builder.add_from_file("./interfaz_entrenamiento.glade")
handlers = {
    "terminar_aplicacion": Gtk.main_quit,
    "seleccionar_carpeta_validacion": seleccionar_carpeta_validacion,
    "seleccionar_carpeta_datos": seleccionar_carpeta_datos,
    "seleccionar_carpeta_guardar": seleccionar_carpeta_guardar,
    "entrenar_red": entrenar_red,
    "cambiar_blanco": cambiar_blanco,
    "cambiar_negro": cambiar_negro,
    "seleccionar_datos_val": seleccionar_datos_val,
    "cancelar_datos_val": cancelar_datos_val,
    "seleccionar_datos": seleccionar_datos,
    "cancelar_datos": cancelar_datos,
    "cancelar_carpeta_guardar": cancelar_carpeta_guardar,
    "guardar_carpeta_guardar": guardar_carpeta_guardar
}
builder.connect_signals(handlers)
window = builder.get_object("ventana_principal")
seleccionador_datos_val = builder.get_object("seleccionador_datos_val")
seleccionador_dato = builder.get_object("seleccionador_dato")
seleccionador_carpeta_guardar = builder.get_object("seleccionador_carpeta_guardar")
ent_ancho = builder.get_object("entrada_ancho")
ent_altura = builder.get_object("entrada_altura")
ent_no_categorias = builder.get_object("entrada_no_categorias")
ent_no_pasos= builder.get_object("entrada_no_pasos")
ent_numero_epocas = builder.get_object("entrada_no_epocas")
ent_lr = builder.get_object("entrada_lr")
ent_pasos_val= builder.get_object("entrada_pasos_val")
ent_tamano_lote = builder.get_object("entrada_tamano_lote")
etq_dir_validacion = builder.get_object("etiqueta_dir_validacion")
etq_dir_datos = builder.get_object("etiqueta_dir_datos")
etq_ruta_guardar = builder.get_object("etiqueta_ruta_guardar")

Datos_entrenamiento = './Imagenes/Entrenamiento'
Datos_validacion = './Imagenes/Validacion'
Carpeta_destino = './modelo'
epocas=20
longitud, altura = 150, 150 #100
batch_size = 32
pasos = 50
Pasos_validacion= 300 #200
filtrosConv1 = 32
filtrosConv2 = 64
Size_filtro1 = (3, 3)
Size_filtro2 = (2, 2)
Size_pool = (2, 2)
clases = 6
learningRate = 0.0004 #0.0005

ent_altura.set_text(str(altura))
ent_ancho.set_text(str(longitud))
ent_numero_epocas.set_text(str(epocas))
ent_no_pasos.set_text(str(pasos))
ent_pasos_val.set_text(str(Pasos_validacion))
ent_no_categorias.set_text(str(clases))
ent_lr.set_text(str(learningRate))
ent_tamano_lote.set_text(str(batch_size))
etq_dir_datos.set_text(Datos_entrenamiento)
etq_dir_validacion.set_text(Datos_validacion)
etq_ruta_guardar.set_text(Carpeta_destino)
window.show_all()
Gtk.main()