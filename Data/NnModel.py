# pip install tensorflow
# pip install h5py
import Data.Utilities as Data
import pandas as pd
import numpy as np
from keras.models import load_model as Load_Model

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils

# getting rid of Tensorflow warnings
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

dataFrame = Data.dataFrame
X_y = {}


def pre_pro_for_modeling(df):
    wsm_df = Data.WSM(df)
    # class_df = df.copy()
    # adding classified column to class_df by index column
    df = pd.merge(df, wsm_df['classified'], left_index=True, right_index=True)
    df = Data.letters_to_numbers(df, columns=['Asset Security Grade'])
    df = Data.unique_to_numbers(df, 'Asset Type')  # {"ip":0,"webapp",1}
    return df


# multy class col to binary multy col
def dummy_y_func(y):
    # encode class values as integers
    encoder = LabelEncoder()
    encoder.fit(y)
    encoded_Y = encoder.transform(y)
    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_Y)
    # print('dummy_y:\n', dummy_y)
    return dummy_y


def modeling(df, class_col='classified'):
    X = df.iloc[:, :6]
    y = df[class_col]
    y = dummy_y_func(y)
    tf.convert_to_tensor(X)
    X_y['X'] = X
    X_y['y'] = y
    model = Sequential()
    model.add(Dense(16, input_dim=6, activation='relu'))
    model.add(Dense(12, activation='relu'))
    model.add(Dense(5, activation='softmax'))

    # compile the keras model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, epochs=50, batch_size=10, shuffle=True,
              validation_split=0.2,
              verbose=1)
    return model


def evaluate_model(model, X, y):
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy * 100))


def predict_model(model, x):
    print(x)
    result = model.predict(x)
    classes = np.argmax(result, axis=1)
    print('result:', classes)


def save_model(model, path):
    model.save(f'{path}NnModel.h5')
    print("Saved model to disk")


def load_model(path):
    model = Load_Model(f'{path}NnModel.h5')
    model.summary()
    return model


#
# class_df = pre_pro_for_modeling(dataFrame)
# model = modeling(class_df, class_col='classified')
# save_model(model,'')
# model=load_model('')
# evaluate_model(model, X_y['X'], X_y['y'])

# predict_model(model,class_df.iloc[0:2,0:6])

from utils import routes

# pd.read_csv('..\\'+routes.status_table,index_col=[0])
# pip3 install -U scikit-learn scipy matplotlib

