import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
import itertools

from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

def build_LSTM(train_X, units, optimizer, loss):
    model = Sequential()
    model.add(GRU(units = units, return_sequences=True, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dropout(0.2))
    model.add(GRU(units = units))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(optimizer, loss)
    return model

def predict_ahead(model,X_test,n_ahead):
    predictions = np.zeros(n_ahead)
    predictions[0] = model.predict(X_test,batch_size = 1)
    
    if n_ahead > 1:
        for i in range(1,n_ahead):
            x_new = np.append(X_test[0][1:],predictions[i-1])
            X_test = x_new.reshape(1,x_new.shape[0],1)
            predictions[i] = model.predict(X_test,batch_size = 1)
    return predictions

def FitForecast(X_train, y_train, X_test, n_ahead, input_size, hidden_units, dropout, val_split, learning_rate, epochs, trained_model):
    model = build_LSTM(input_size,hidden_units,dropout, learning_rate)

    if trained_model is not None:
        model.set_weights(weights = trained_model.get_weights())

    history = model.fit(x=X_train, y=y_train, batch_size=1, epochs=epochs, verbose=1, validation_split=val_split, shuffle=False)

    predictions = predict_ahead(model,X_test,n_ahead)
    return model, predictions, history