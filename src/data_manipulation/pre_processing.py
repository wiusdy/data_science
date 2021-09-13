import matplotlib as plt
import seaborn as sns
from data_structure.structure_data import DataStructure



class PreProcessing(object):
    def __init__(self):
        self.data_structured = DataStructure()
        self.data = self.data_structured.build_data()
        