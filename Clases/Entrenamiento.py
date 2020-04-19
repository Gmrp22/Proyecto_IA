import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as Back


Back.clear_session()



Datos_entrenamiento = './Imagenes/Entrenamiento'
Datos_validacion = './Imagenes/Validacion'


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


##Preparamos nuestras imagenes

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

#RED CONVU
cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, Size_filtro1, padding ="same", input_shape=(longitud, altura, 3), activation='relu'))


cnn.add(MaxPooling2D(pool_size=Size_pool))

cnn.add(Convolution2D(filtrosConv2, Size_filtro2, padding ="same"))
#cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ="same", activation='relu'))
cnn.add(MaxPooling2D(pool_size=Size_pool))
#CLASIFICACION