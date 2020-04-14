from tensorflow.keras import backend as Backend

#ATRIBUTOS
No_epocas=20
longitud= 150
altura = 150 #100
batch_size = 32
No_pasos = 50
Pasos_validacion = 300 #200
Filtro_C1 = 32
Filtro_C2 = 64
Tam_filtro1 = (3, 3)
Tam_filtro2 = (2, 2)
Tam_pool = (2, 2)
clases = 6


#METODOS
def Limpiar_Sesion():
    Backend.clear_session()

