import os
import sys
sys.path.append(os.pardir)
from libs.set_config import SetConfig

if __name__ == "__main__":
    fname = "../config.yaml"
    set_config = SetConfig(fname)
    print("train data fname:", set_config.train_data_fname)
    print("test  data fname:", set_config.test_data_fname)
