import numpy as np
import pandas as pd
import re


class DataStructure(object):
    #this object was created to read all the data and construct a simple dict with all data stuctured
    # Example:
    # 30 CAP | BUPROPIONA CLORIDRATO  150MG,2020-08-05 23:19:09,1,47.5297,39.9
    # 60 CAP | FINASTERIDA 1:10  1MG,2020-08-05 22:51:09,1,46.962,43.6
    
    # Becomes keys and values from each data

    def __init__(self):
        self.data_path = '../data/dados_preco.csv'
    
    def read_data(self):
        try:
            data_frame = pd.read_csv(self.data_path, delimiter=',')
            return data_frame            
        except Exception as error:
            return None
    
    def build_data(self):
        data_frame = self.read_data()
        if data_frame is not None:
            data = []          
            for description, data_created, qtd_input, calcule, true_calcule in zip(data_frame['descricao'], 
                                                                                    data_frame['criado'], 
                                                                                    data_frame['qtdInsumos'], 
                                                                                    data_frame['calculado'], 
                                                                                    data_frame['correto']):
                
                if description is not None and \
                    data_created is not None and \
                    qtd_input is not None and \
                    calcule is not None and\
                    true_calcule is not None:


                    qtd_unit_vol, inputs = self.process_description(description)
                    sample = {
                    'description': {
                        'unit_volume': qtd_unit_vol, #always in CAP
                        'insumos': inputs,

                    },
                    'criado': data_created,
                    'qtd_insumo': float(qtd_input),
                    'calculo': float(calcule),
                    'true_calculo': float(true_calcule)
                    }
                    data.append(sample)
                


        else:
            raise Exception('Could not read the data to filter')
        
        return data
    
    def process_description(self, description):

        qtd_unit_vol = float(description.split('|')[0].replace('CAP', ''))
        inputs_metadata = description.split('|')[-1]
        input_data = inputs_metadata.split(';')
        inputs = []
        for input in input_data:
            input_metadata = input.split(' ')
            input_metadata_mg = input_metadata[-1]
            input_mg = re.findall('[-+]?\d*\.\d+|\d+', str(input_metadata_mg))
            input_name = input.replace(str(input_metadata_mg), '')
            data = {'input_name':input_name,
                    'mg_unit': float(''.join(input_mg))}
            inputs.append(data)
        
        return qtd_unit_vol, inputs       




