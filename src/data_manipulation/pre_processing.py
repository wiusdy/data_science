import matplotlib as plt
import numpy as np
import seaborn as sns
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
                

        