from data_manipulation.pre_processing import PreProcessing

def main():
    preprocessing = PreProcessing()
    filtered, number_of_filtered = preprocessing.filter_by_qtd_input(5, bigger=False)
    print(filtered, number_of_filtered)

if __name__ == '__main__':
    main()