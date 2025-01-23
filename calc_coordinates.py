import os 
import sys
sys.path.append(os.pardir)
from libs.deepimfam import DeepImFam

if __name__ == "__main__":
    fname = "config.yaml"
    deepimfam = DeepImFam(fname)
    index = "AURR980113"
    aaindex1 = deepimfam.load_amino_vectors(index)
    print("+++ vectors {} +++".format(index))
    print(aaindex1)
    
    print("+++ calcurate coordinates +++")
    deepimfam.calc_coordinates(index)