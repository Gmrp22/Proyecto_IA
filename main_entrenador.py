from gi.repository import Gtk

def seleccionar_carpeta_validacion(button):
    seleccionador_datos_val.show_all()
def seleccionar_carpeta_datos(button):
    seleccionador_dato.show_all()
def seleccionar_carpeta_guardar(button):
    seleccionador_carpeta_guardar.show_all();
def entrenar_red(button):
    print("hola")
def seleccionar_datos_val(button):
    print("hola")
def cancelar_datos_val(button):
    seleccionador_datos_val.hide()
def seleccionar_datos(button):
    print("hola")
def cancelar_datos(button):
    seleccionador_dato.hide()
def cancelar_carpeta_guardar(button):
    seleccionador_carpeta_guardar.hide()
def guardar_carpeta_guardar(button):
    print("hola")
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
ent_altura.set_text(str(150))
ent_ancho.set_text(str(150))
ent_numero_epocas.set_text(str(20))
ent_no_pasos.set_text(str(50))
ent_pasos_val.set_text(str(50))
ent_no_categorias.set_text(str(6))
ent_lr.set_text(str(0.0004))
ent_tamano_lote.set_text(str(32))
etq_dir_datos.set_text("./Imagenes/Entrenamiento")
etq_dir_validacion.set_text("./Imagenes/Validacion")
etq_ruta_guardar.set_text("./Modelo")
window.show_all()
Gtk.main()