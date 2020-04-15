from gi.repository import Gtk

    
def seleccionar(button):
    print('seleccionar')
    
def seleccionar_foto(button):
    selector.show_all()

def cancelar(button):
    print('cancelar')
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
    "seleccionar": seleccionar,
    "seleccionar_archivo": seleccionar_foto,
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
window.show_all()
Gtk.main()