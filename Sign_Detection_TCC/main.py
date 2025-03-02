## REDE CNN

import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from tensorflow import keras
from keras.layers import Dropout, Flatten
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import os

## tf versão 2.13.0
##keras versão 2.13.1

### Parâmetros
path = "Imagens"
batch_size_val = 30
steps_per_epoch_val = 200
epochs_val = 50
imageDimesions = (32, 32, 3)

## Importar Imagens
count = 0
images = []
classNo = []
pastas = os.listdir(path)
print("Total de Classes:", len(pastas))
noOfClasses = len(pastas)

for pt in range(0, len(pastas)):
    arquivos = os.listdir(path + "/" + str(count))
    for arq in arquivos:
        curImg = cv2.imread(path + "/" + str(count) + "/" + arq)
        images.append(curImg)
        classNo.append(count)

    count += 1

images = np.array(images)
classNo = np.array(classNo)

#### Converter imagens para escala de cinza
##gray_images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in images]
##gray_images = np.array(gray_images)
##gray_images = gray_images.reshape(gray_images.shape[0], 32, 32, 1)  # Adicione um canal para imagens em escala de cinza

## Separando Imagens
X_train, X_test, y_train, y_test = train_test_split(images, classNo, test_size=0.2)
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.2)


## Funções do pré-processamento das Imagens

def grayscale(imgToGray):
    grayImg = cv2.cvtColor(imgToGray, cv2.COLOR_BGR2GRAY)
    return grayImg

def equalize(imgToEq):
    eqImg = cv2.equalizeHist(imgToEq)
    return eqImg

def preprocessing(imgToPreprocess):
    grayImg = grayscale(imgToPreprocess)
    eqImg = equalize(grayImg)
    processedImg = eqImg / 255
    return processedImg

## Pré-processar imagens
X_train = np.array(list(map(preprocessing, X_train)))
X_validation = np.array(list(map(preprocessing, X_validation)))
X_test = np.array(list(map(preprocessing, X_test)))

## Regularizar Arrays
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
X_validation = X_validation.reshape(X_validation.shape[0], X_validation.shape[1], X_validation.shape[2], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)

## Aumentando Imagens com ImageDataGenerator
dataGen = ImageDataGenerator(width_shift_range=0.2,  # alterar posição width da imagem
                             height_shift_range=0.2,  # alterar posição hight da imagem
                             zoom_range=0.2,  # colocar zoom
                             shear_range=0.2,  # mudar ângulo
                             rotation_range=10)  # rotacionar imagem
dataGen.fit(X_train)
batches = dataGen.flow(X_train, y_train, batch_size=20)
X_batch, y_batch = next(batches)

y_train = tf.keras.utils.to_categorical(y_train, noOfClasses)
y_validation = tf.keras.utils.to_categorical(y_validation, noOfClasses)
y_test = tf.keras.utils.to_categorical(y_test, noOfClasses)

class_names = ['20km/h', '30km/h', '50km/h', '60km/h', '70km/h', '80km/h', '100km/h', '120km/h', 'Pare']
## Criar Modelo
def myModel():
    model = Sequential([
    keras.layers.Conv2D(32, kernel_size=(5, 5), activation='relu', input_shape=(32, 32, 1)),
    keras.layers.MaxPooling2D(2, 2),

    keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Dropout(0.5),

    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(noOfClasses, activation='softmax'),
 ])
    # COMPILE MODEL
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


## Treinamento
model = myModel()
print(model.summary())

history = model.fit(dataGen.flow(X_train, y_train, batch_size=batch_size_val),
                              steps_per_epoch=steps_per_epoch_val, epochs=epochs_val,
                              validation_data=(X_validation, y_validation), shuffle=1)


## Mostrar histórico de treinamento
plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Treinamento', 'Validacao'])
plt.title('Erro')
plt.xlabel('Epocas')
plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['Treinamento', 'Validacao'])
plt.title('Acuracia')
plt.xlabel('Epocas')
plt.show()
score = model.evaluate(X_test, y_test, verbose=0)
print('Test Score:', score[0])
print('Test Accuracy:', score[1])

## Salvar modelo
model.save('modelo.h5')
print('Modelo Salvo!')