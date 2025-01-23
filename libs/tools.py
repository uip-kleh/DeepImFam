import os
import sys
import json
import numpy as np
import pandas as pd

class Tools:
    def __init__(self):
        pass
    
    # IO TOOLS
    def load_json(self, fname) -> dict:
        with open(fname, "r") as f:
            return json.load(f)
        
    def save_dict_as_df(self, d: dict, fname) -> None :
        pd.DataFrame(d).to_csv(fname, index=False, header=True)
        
    # CALCURATION TOOLS
    def standarize(self, values: np.array) -> np.array:
        print(values)
        return (values - np.mean(values)) / np.std(values) 
    
    def normalize(self, values: np.array):
        return (values - np.min(values)) / (np.max(values) - np.min(values))