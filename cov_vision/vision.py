import tensorflow as tf
import numpy as np
from glob import glob
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.optimizers import Adam
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

IMAGE_DIM = (200,125)

filenames_infected = glob("Healthy_jpg/*.jpg")
filenames_healthy = glob("Healthy_jpg/*.jpg")

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

# try using Jupyter notebook, Colab
np.set_printoptions(threshold=sys.maxsize) 
print(train_x[0].shape)
print(train_y[0].shape)

# view_image(train_x[0])
train_x = train_x.reshape(train_x.shape[0], IMAGE_DIM[0], IMAGE_DIM[1], 1)

EPOCHS = 10
LEARNING_RATE = 0.1

# try conv -> pooling -> conv -> pooling -> flatten -> dense -> dense
# pooling done with MaxPooling2D
# also use dropout?
# not deep enough?
# use pre-trained
# dropout should be used when loss is high
# do it in the cloud - faster (e.g. colab)
model = Sequential()
model.add(Conv2D(64, kernel_size=4, activation="relu", input_shape=(IMAGE_DIM[0],IMAGE_DIM[1], 1)))
model.add(MaxPooling2D(4,4))
model.add(Conv2D(32, kernel_size=3, activation="relu"))
model.add(MaxPooling2D(3,3))
model.add(Flatten())
model.add(Dense(32))
model.add(Dense(1, activation='softmax'))

print(model.summary())

model.compile(optimizer=Adam(LEARNING_RATE), loss="binary_crossentropy", metrics=["accuracy"])
model.fit(train_x, train_y, epochs=EPOCHS, shuffle=True)

model.save("lung_model.h5")