from re import X
from data_manipulation.pre_processing import PreProcessing

def pre_process_data():
    preprocessing = PreProcessing()
    matrix = preprocessing.all_data_one_table()
    data_frame = preprocessing.matrix_to_pandas_data_frame(matrix)
    return preprocessing.get_trainable_data(data_frame)

def main():
    X_Train, X_Test = pre_process_data()
    
    
    

if __name__ == '__main__':
    main()