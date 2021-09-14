import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np


class Model(object):

    def __init__(self, X_train, Y_train, X_test, Y_test):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        self.regressor = LinearRegression()
    
    def train(self):
        self.regressor.fit(self.X_train, self.Y_train)
        print('RESULTADOS DE TREINO')
        print(self.regressor.intercept_)
        print(self.regressor.coef_)
    
    def test(self):
        y_pred = self.regressor.predict(self.X_test)
        
        print('RESULTADOS DE TESTE')
        print('Erro médio absoluto:', metrics.mean_absolute_error(self.Y_test, y_pred))
        print('Erro médio quadrado:', metrics.mean_squared_error(self.Y_test, y_pred))
        print('Raiz do erro médio quadrado:', np.sqrt(metrics.mean_squared_error(self.Y_test, y_pred)))
    

    

    