import tensorflow as tf
import numpy as np
from glob import glob
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from PIL import Image
from matplotlib import pyplot as plt
import sys

def view_image(img):
    '''
    Shows an image. Image must be entered as a numpy array.
    '''
    plt.imshow(img)
    plt.show()

def preprocess_image(pil_image):
    '''
    Preprocesses or prepares a PIL image for the model.
    '''
    return np.array(pil_image.convert("L"))/255.0

def load_data():    
    filenames_infected = glob("Infected-jpg/*.jpg")
    filenames_healthy = glob("Healthy-jpg/*.jpg")
    
    # INPUT
    # array of images (each in the form of a numpy array)
    train_infected_x = np.array([preprocess_image(Image.open(filename)) for filename in filenames_infected])
    train_healthy_x = np.array([preprocess_image(Image.open(filename)) for filename in filenames_healthy])

    # LABELS
    # 0: healthy 1: infected
    train_healthy_y = np.array([0 for img in train_healthy_x])
    train_infected_y = np.array([1 for img in train_infected_x])

    # combine the arrays together
    train_x = np.array(np.append(train_infected_x, train_healthy_x, axis=0))
    train_y = np.array(np.append(train_infected_y, train_healthy_y, axis=0))

    return train_x, train_y

def new_model(x, y, epochs=10, learning_rate=0.1):
    train_x = x.reshape(x.shape[0], IMAGE_DIM[0], IMAGE_DIM[1], 1)
    train_y = y

    # try conv -> pooling -> conv -> pooling -> flatten -> dense -> dense
    # pooling done with MaxPooling2D
    # also use dropout?
    # not deep enough?
    # use pre-trained
    # dropout should be used when loss is high
    # do it in the cloud - faster (e.g. colab)
    #
    # 1. try more layers
    # 2. try other, larger dataset

    # for now, figure out how to properly structure the model

    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation="relu", input_shape=(IMAGE_DIM[0], IMAGE_DIM[1], 1), padding='same'))
    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3), activation="relu", padding='same'))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(32, activation="relu"))
    model.add(Dense(1, activation="softmax"))

    model.compile(optimizer=Adam(learning_rate), loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(train_x, train_y, epochs=epochs, shuffle=True)

    model.save("lung_model.h5")

    return model

IMAGE_DIM = (200,125)

train_x, train_y = load_data()
train_x = train_x.reshape(train_x.shape[0], IMAGE_DIM[0], IMAGE_DIM[1], 1)

model = load_model("lung_model.h5")

print(model.predict(train_x))