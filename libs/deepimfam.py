import os 
import sys
sys.path.append(os.pardir)
import numpy as np
from tqdm import tqdm
from libs.set_config import SetConfig
from libs.tools import Tools

class DeepImFam(SetConfig, Tools):
    def __init__(self, fname):
        SetConfig.__init__(self, fname)
        Tools.__init__(self)
        self.load_aaindex1()

    # CALCURATE COORDINATES 
    def calc_coordinates(self, index_name: str):
        index = self.load_amino_vectors(index_name)
        sequences = self.load_sequnces()
        for i, seq in enumerate(tqdm(sequences)):
            x = 0
            y = 0
            coordinate_x = []
            coordinate_y = []
            for c in seq: 
                if not c in index:
                    continue
                x += index[c]
                y += 1
                coordinate_x.append(x)
                coordinate_y.append(y)
            fname = os.path.join(self.coordinates_path, str(i) + ".dat")
            coordinate = {"x": coordinate_x, "y": coordinate_y}
            self.save_dict_as_df(coordinate, fname)
            # print(fname)                

    def load_sequnces(self) -> list:
        return self.load_seq(self.amino_train_path) + self.load_seq(self.amino_test_path)
                
    def load_seq(self, fname) -> list:
        with open(fname, "r") as f:
            aaseq = [l.split()[-1] for l in f.readlines()]
        return aaseq
    
    def load_aaindex1(self):
        self.aaindex1 = self.load_json(self.aaindex1_path)

    def load_amino_vectors(self, index_name: str) -> dict:
        index: dict = self.aaindex1[index_name]
        std_values = self.standarize(np.array(list(index.values())))
        std_index = {}
        for i, key in enumerate(index.keys()):
            std_index[key] = std_values[i]
        return std_index
    
    