from data_manipulation.pre_processing import PreProcessing
from model.model import Model
import matplotlib.pyplot as plt

def pre_process_data(as_one_table=False):
    preprocessing = PreProcessing()
    if as_one_table:
        matrix = preprocessing.all_data_one_table()
    else:
        matrix = preprocessing.build_data_as_samples()
    data_frame = preprocessing.matrix_to_pandas_data_frame(matrix)
    print('---------------------------------------DATASET DESCRIPTION------------------------------------------')
    print(data_frame.describe())
    return preprocessing.get_trainable_data(data_frame, scale=True)

def main():

    X_Train, X_Test, Y_Train, Y_Test = pre_process_data(as_one_table=False)
    model = Model(X_Train, Y_Train, X_Test, Y_Test)
    model.train()
    model.test()
    
if __name__ == '__main__':
    main()