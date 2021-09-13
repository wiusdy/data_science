from traceback import print_exc
import numpy as np
import pandas as pd


class DataStructure(object):
    #this object was created to read all the data and construct a simple dict with all data stuctured
    # Example:
    # 30 CAP | BUPROPIONA CLORIDRATO  150MG,2020-08-05 23:19:09,1,47.5297,39.9
    # 60 CAP | FINASTERIDA 1:10  1MG,2020-08-05 22:51:09,1,46.962,43.6
    
    # Becomes keys and values from each data

    def __init__(self):
        self.data_path = '../../data/dados_preco.csv'
    
    def read_data(self):
        try:
            data_frame = pd.read_csv(self.data_path, delimiter=',')
            return data_frame            
        except Exception as error:
            return None
    
    def filter_data(self):
        data_frame = self.read_data()
        if data_frame is not None:
            pass
        else:
            raise Exception('Could not read the data to filter')
            


data = DataStructure()
data_frame = data.filter_data()



