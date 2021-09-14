import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from data_structure.structure_data import DataStructure


class PreProcessing(object):
    def __init__(self):
        self.data_structured = DataStructure()
        self.data = self.data_structured.build_data()
    
    def filter_by_input(self, input):
        filtered = []
        for data in self.data:
            description = data['description']
            inputs = description['insumos']
            data['description']['insumos'] = []
            for input_ in inputs:
                if input_['input_name'] == input:
                    data['description']['insumos'] = input_                 
                    filtered.append(data)
        return filtered, len(filtered)
    
    def filter_by_qtd_input(self, qtd_input, bigger=True):
        filtered = []
        for data in self.data:
            if data['qtd_insumo'] >= qtd_input and bigger is True:
                filtered.append(data)
            if data['qtd_insumo'] < qtd_input and bigger is False:
                filtered.append(data)
        return filtered, len(filtered)
    
    def all_data_one_table(self):
        matrix_data = []        
        for data_idx, data in enumerate(self.data):
            description = data['description']
            for input in description['insumos']:
                sample = {
                        'insumo': input['input_name'], 
                        'vol_und': data['description']['unit_volume'],  
                        'mg_und': input['mg_unit'], 
                        'criado': data['criado'],
                        'qtd_insumo': data['qtd_insumo'],
                        'calculo': data['calculo'],
                        'true_calcule': data['true_calculo'],
                        'calcule_distance_error': data['calcule_distance_error']}
                matrix_data.append(sample)
        return matrix_data

    def matrix_to_pandas_data_frame(self, matrix):
        only_values = []
        columns = matrix[0].keys()
        for line in matrix:
            only_values.append(line.values())
        return pd.DataFrame(only_values, columns=columns)
    
    def get_trainable_data(self, data_frame):
        data_frame = data_frame.drop('insumo', axis=1)
        data_frame = data_frame.drop('criado', axis=1)        
        x = data_frame.values 
        min_max_scaler = preprocessing.MinMaxScaler()
        scaled_data = min_max_scaler.fit_transform(x)
        
        X_train = scaled_data[:5121, :5]
        X_test = scaled_data[5122:, :5]
        return X_train, X_test
                

            

                

        